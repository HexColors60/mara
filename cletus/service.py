"""
Cletus process manager

Controls settings, server, and loaded modules
"""
from collections import defaultdict
import datetime
import inspect
from modulefinder import ModuleFinder
import sys
import time

from .settings import Settings
from .settings import defaults as default_settings
from .connection import Server
from .logger import Logger
from . import events
from . import storage
from . import timers


class Service(object):
    """
    Service management
    """
    def __init__(self):
        # Store settings
        self.settings = None
        
        # No server yet
        self.server = None
        
        # Store of stores
        self.stores = defaultdict(dict)
        
        # Consistent time for events and timers
        self.time = time.time()
        
        # Initialise events
        self.events = defaultdict(list)
        
        # Initialise timers
        self.timers = timers.Registry(self)
        
        # An empty log
        self.log = None
    
    datetime = property(
        fget = lambda self: datetime.datetime.fromtimestamp(self.time),
        doc = "Get the current time as a datetime object"
    )
    
    clients = property(lambda self: self.server._clients.values())
    
    def run(self, *args, **kwargs):
        """
        Collect settings and start the service
        """
        # Collect settings
        self._collect_settings(*args, **kwargs)
        
        # Initialise service tools
        self.log = Logger(self.settings)
        
        # Start the server
        self._start()
        

    #
    # Events
    #
    
    def listen(self, event_class, handler=None):
        # Called directly
        if handler:
            return self.events[event_class].append(handler)

        # Called as a decorator
        def decorator(fn):
            self.events[event_class].append(fn)
            return fn
        return decorator
    
    def trigger(self, event):
        # Make sure all listeners have access to the service, in case they're
        # defined out of scope
        event.service = self
        
        self.log.event(event)
        for handler in self.events[event.__class__]:
            if event.stopped:
                return
            if inspect.isgeneratorfunction(handler):
                generator = handler(event)
                try:
                    generator.next()
                except StopIteration:
                    pass
                else:
                    if hasattr(event, 'client'):
                        event.client.capture(generator)
            else:
                handler(event)
    
    #
    # Timers
    #
    
    def timer(self, cls=timers.PeriodTimer, **kwargs):
        """
        Function decorator to define a timer
        """
        def wrap(fn):
            timer = cls(**kwargs)
            timer.fn = fn
            self.timers.add(timer)
            return fn
        return wrap


    #
    # Server operations
    #
    
    def write(self, clients, *data):
        if not hasattr(clients, '__iter__'):
            clients = [clients]
        for client in clients:
            client.write(*data)
    
    def write_all(self, *data, **kwargs):
        # Get client list
        clients = self.get_all(**kwargs)
        
        # Write data to the clients
        for client in clients:
            client.write(*data)
    
    def get_all(self, **kwargs):
        """
        Get a list of clients, filtered by the global filter, a local filter
        and an exclude list
        """
        # Capture kwargs
        filter_fn = kwargs.pop('filter', None)
        exclude = kwargs.pop('exclude', [])
        if kwargs:
            raise ValueError('Unexpected keyword arguments: %s' % kwargs)
        if not hasattr(exclude, '__iter__'):
            exclude = [exclude]
            
        # Filter the client list using global filter and exclude list
        clients = self.filter_all(
            self,
            (client for client in self.clients if client not in exclude),
            **kwargs
        )
        
        # Further filtering for this call
        if filter_fn:
            clients = filter_fn(self, clients, **kwargs)
        
        return clients
        
    
    @staticmethod
    def _filter_all_default(service, clients, **kwargs):
        return clients
    _filter_all = _filter_all_default
    
    @property
    def filter_all(self):
        return self._filter_all
    
    @filter_all.setter
    def filter_all(self, value):
        if value is None:
            value = self._filter_all_default
        elif not callable(value):
            raise ValueError('Filter must be a callable')
        self._filter_all = value
        
    
    #
    # Internal operations
    #
    
    def _collect_settings(self, *args, **kwargs):
        """
        Collect settings
        """
        # Start with default settings
        self.settings = Settings()
        self.settings.load(default_settings)
        
        # Load settings from fn arguments
        self.settings.load(*args)
        self.settings.update(kwargs)
        
        # Load settings from command line
        argv = sys.argv[1:]
        cmd_args = []
        cmd_kwargs = {}
        for arg in argv:
            if arg.startswith('--'):
                if '=' in arg:
                    key, val = arg[2:].split('=', 1)
                    cmd_kwargs[key] = val
                elif arg.startswith('--no-'):
                    cmd_kwargs[arg[5:]] = False
                else:
                    cmd_kwargs[args[2:]] = True
            else:
                cmd_args.append(arg)
        self.settings.load(*cmd_args)
        self.settings.update(cmd_kwargs)
    
    def _start(self):
        """
        Start the server
        """
        # Inform that we're starting
        self.log.service('Service starting')
        self.trigger(events.PreStart())
        
        # Start server
        self.server = Server(self)
        self.server.listen()
        self.trigger(events.PostStart())
        
    def poll(self):
        """
        A poll from the server
        """
        # Update time
        self.time = time.time()
        
        # Call due and overdue timers
        self.timers.trigger()
    
    def stop(self):
        """
        Stop the server
        """
        self.trigger(events.PreStop())
        self.server.shutdown()
        self.log.service('Service stopped')
        self.trigger(events.PostStop())

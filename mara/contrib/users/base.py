"""
Mara users
"""
import re

from ..commands import define_command
from ... import events
from ... import storage
from ... import util


def event_add_user(event):
    """
    Add user object to events (when available)
    """
    event.user = getattr(event.client, 'user', None)


class ClientField(storage.Field):
    """
    Manage the client.user attribute
    """
    def deserialise(self, obj, name, data):
        print "DESERIALISNG THE CLIENT"
        super(ClientField, self).deserialise(obj, name, data)
        
        # Link this client to this user
        client = self.get_value(obj, name)
        print "Linking user.client", obj, client
        if client:
            client.user = obj
            

class UserManager(storage.Manager):
    def get_active_by_name(self, names):
        active = self.active()
        lower_names = [name.lower() for name in names]
        found = { k: v for k, v in active.items() if k in lower_names }
        missing = set(lower_names).difference(set(found.keys()))
        if missing:
            raise ValueError(
                'Unknown users %s' % util.pretty_list(list(missing))
            )
        return found


class BaseUser(storage.Store):
    abstract = True
    manager = UserManager()
    
    client = ClientField(session=True)
    name = storage.Field('')
    
    def write(self, *lines):
        self.client.write(*lines)
    
    def disconnect(self):
        """
        Call to disconnect the user
        """
        # Tell the client to close
        self.client.close()
        
    def disconnected(self):
        """
        Clean up User object when a user disconnects
        """
        # Manually break circular reference for efficient garbage collection
        self.client = None
        
        # Remove from active list
        self.manager.remove_active(self)


@define_command(help='List all users')
def cmd_list_users(event):
    """
    List admin users
    
    Needs the user class in context as: context={'User': User}
    """
    User = event.context['User']
    
    online = [user.name for user in sorted(User.manager.active().values())]
    offline = [user.name for user in sorted(User.manager.saved().values())]
    event.user.write(
        util.HR('Users'),
        'Online: ' + util.pretty_list(online),
        'Offline: ' + util.pretty_list(offline),
        util.HR(),
    )


class ConnectHandler(events.Handler):
    """
    Connect handler to collect a user's name and welcome them to the service
    
    Usage::
        
        service.listen(events.Connect, ConnectHandler(User))
    """
    user_store = None
    
    # Initial welcome message
    msg_welcome_initial = 'Welcome!'
    name_prompt = 'What is your name? '
    name_error = 'Your name can only contain the letters a-z'
    
    # Message sent to old connection when reconnecting
    msg_reconnect_old = 'You have logged in from a different connection.'
    
    # Message sent to user when they finish connecting
    #   name    user's name
    #   others  list of other users present
    #   are     correct version of is/are for the ``others`` list
    msg_welcome_complete = 'Welcome, %(name)s! %(others)s %(are)s here'
    
    # If nobody else is here, this is used for ``others``
    msg_no_others = 'Nobody else'
    
    # Announcement messages for connecting and reconnecting
    #   name    user's name
    msg_announce_connect = '-- %(name)s has connected --'
    msg_announce_reconnect = '-- %(name)s has reconnected --'
    
    def __init__(self, user_store):
        self.user_store = user_store
    
    def handler_10_get_name(self, event):
        """
        Welcome the user and ask their name
        """
        event.client.write(self.msg_welcome_initial)
        event.client.write('')
        event.client.write_raw(self.name_prompt)
        name = yield
        
        # Validate name
        if re.search(r'[^a-zA-Z]', name):
            # Invalid
            event.client.write(self.name_error)
            self.handlers = self.get_handlers()
        
        # Name collected, store on self
        self.name = name

    def handler_20_get_user(self, event):
        """
        Turn name into a user object
        
        Only works if your user is a session store; permanent user stores will
        need some authentication, eg contrib.users.password.ConnectHandler
        """
        User = self.user_store
        if not issubclass(User, storage.SessionStore):
            raise ValueError('Permanent user stores should use authentication')
        
        self.user = User.manager.load(name)
        if not self.user:
            self.user = User(name)
            self.user.name = self.name
        self.user.save()
    
    def handler_80_attach_user(self, event):
        """
        Attach user object to client
        """
        # Attach user to client
        event.client.user = self.user

        # Attach client to user (clearing old client if one present)
        self.reconnecting = False
        if self.user.client:
            self.user.client.user = None
            self.user.client.write(self.msg_reconnect_old)
            self.user.client.close()
            self.reconnecting = True
        self.user.client = event.client
    
    def handler_90_announce_user(self, event):
        """
        Announce user's arrival
        """
        # Find others here
        others = [
            client.user.name
            for client in event.service.filter_clients(exclude=event.client)
        ]
        if not others:
            others = [self.msg_no_others]
        
        # Welcome user
        event.client.write(self.msg_welcome_complete % {
            'name':     self.user.name,
            'others':   util.pretty_list(sorted(others)),
            'are':      'is' if len(others) == 1 else 'are',
        })
        
        # Announce to everyone else
        msg_announce = self.msg_announce_connect
        if self.reconnecting:
            msg_announce = self.msg_announce_reconnect
            
        event.service.write_all(
            msg_announce % {'name': self.user.name},
            exclude=event.client,
        )


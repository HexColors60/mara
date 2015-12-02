=========
Upgrading
=========

For an overview of what has changed between versions, see the :ref:`changelog`.

Instructions
============

Upgrading from 0.4.0
--------------------

The class ``mara.service.Service`` now inherits from
``container.ClientContainer``, which means the ``get_all`` attribute has been
renamed to ``filter_clients``.

The class ``mara.storage.StoreField`` has been removed; replace your use of it
with the normal ``mara.storage.Field``, which can now automatically serialise
and deserialise references to ``Store`` instances. The field now also supports
the use of store instances in list and dict values.

Client serialisers have been removed; you should now write custom fields with
their own ``serialise`` and ``deserialise`` methods, which can then set
attributes on the client object; see ``ClientField`` in
:source:`mara/contrib/useres/base.py` for an example.


.. _changelog:

Changelog
=========

0.5.0, In development
---------------------
Feature:

* Added class-based event handlers, with support for use as command functions
* Added client containers
* Added room support
* Removed ClientSerialiser, replaced with improved Field serialiser
* Removed StoreField, replaced with improved Field serialiser


0.4.0, 2015-11-21
-----------------
Feature:

* Renamed project
* Added angel to support seamless restarts

Internal:

* Added root_path setting for more reliable relative paths


0.3.0, 2015-02-16
-----------------
Feature:

* Restructured from plugin-based command to framework


0.2.1, 2012-01-20
-----------------
Feature:

* Extra commands in plugins

Internal:

* Better command error handling - now piped to users
* Plugins now private namespaces with shared dict 'publics'


0.2.0, 2012-01-18
-----------------
Feature:

* Added telnet negotiation
* Added socials

Internal:

* Added support for different newline types
* Split User into User and Client objects
* Added argument parsing to Command object


0.1.1, 2012-01-16
-----------------
Internal:

* Rearranged plugin files to improve clarity
* Internal: Plugin lists


0.1.0, 2012-01-15
-----------------
Feature:

* Events, plugins
* IRC- and MUD-style chat

Internal:

* Moved all non-core code into plugins


0.0.1, 2012-01-13
-----------------
Feature:

* Initial release of new version in python


email-validator
===============

Checks if an e-mail address exists or not.

Installation
------------

::

    pip install evalidator

Those who can't wait for the next release:

::

    python setup.py install

Command-line Usage
------------------

::

    $ evalidate someone@email.com

This will tell you if the given e-mail address exists on the internet or
not.

Library Usage
-------------

::

    >>> import evalidator
    >>> evalidator.validate('someone@email.com')

Supported Services:
-------------------

At the moment only Google and Yahoo! Mail work. Please open a new issue
if you would like to validate e-mail addresses for some other e-mail
service.

License
-------

``The MIT License``

email-validator
===============

|Build Status|

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

Supported Services
------------------

- Google Mail
- Yahoo! Mail

Please open a new issue if you would like to validate e-mail
addresses for some other e-mail service.

License
-------

``The MIT License``

.. |Build Status| image:: https://travis-ci.org/ritiek/scribd-downloader.svg?branch=master
   :target: https://travis-ci.org/ritiek/scribd-downloader

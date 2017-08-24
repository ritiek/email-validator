**This tool is unnecessary work! There is a `better
tool <https://github.com/syrusakbary/validate_email>`__
I did not know about earlier that uses SMTP
replies to validate e-mails and works for any service.**

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

(where `@email.com` is one of below supported services)

This will tell you if the given e-mail address exists on the internet or
not.

Library Usage
-------------

::

    >>> import evalidator
    >>> evalidator.validate('someone@email.com')

(where `@email.com` is one of below supported services)

Supported Services
------------------

- Google Mail (@gmail.com)
- Yahoo! Mail (@yahoo.com)

Please open a new issue if you would like to validate e-mail
addresses for some other e-mail service.

License
-------

``The MIT License``

.. |Build Status| image:: https://travis-ci.org/ritiek/email-validator.svg?branch=master
   :target: https://travis-ci.org/ritiek/email-validator

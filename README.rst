PRA Request Tracker
===================

Public Records Act Request Tracker

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Running the app locally
^^^^^^^^^^^^^^^^^^^^^

* To run the app locally. This will automagically restart for you when you make changes::

    $ docker compose --file=local.yml up

This will capture your console with logs as well.

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command in a separate console::

    $ docker compose --file=local.yml run django python manage.py createsuperuser

In your console that is running `dc up` you'll see a message similar to the following::

    django      | Content-Type: text/plain; charset="utf-8"
    django      | MIME-Version: 1.0
    django      | Content-Transfer-Encoding: 7bit
    django      | Subject: [PRA Request Tracker] Please Confirm Your E-mail Address
    django      | From: webmaster@localhost
    django      | To: admin@example.com
    django      | Date: Tue, 29 Jun 2021 17:35:16 -0000
    django      | Message-ID: <162498811644.12.3635293736420768765@2190a548b587>
    django      | 
    django      | Hello from PRA Request Tracker!
    django      | 
    django      | You're receiving this e-mail because user admin has given your e-mail address to register an account on twitter.com/TechBlocSEA.
    django      | 
    django      | To confirm this is correct, go to http://localhost:8000/accounts/confirm-email/MQ:1lyHdk:Td8HDxKa67J4uKIZdVlx6YsisvdjMS8Psjz95e94Yuw/
    django      | 
    django      | Thank you for using PRA Request Tracker!
    django      | twitter.com/TechBlocSEA
    django      | ------------------------------------------------------------------------------

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy pra_request_tracker

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html




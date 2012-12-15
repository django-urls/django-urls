django-urls
===========

Manage URL Patterns and Views via the Django admin.

## Screenshots

![django-urls screenshot](https://raw.github.com/django-urls/django-urls/master/screenshot.png "")

## Requirements

* Django `1.4.x`.

## Installation

    git clone https://github.com/django-urls/django-urls.git
    cd django-urls
    mkvirtualenv django-urls
    pip install --requirement=requirements.txt
    cd django_urls
    ./manage.py syncdb --noinput
    ./manage.py runserver

Go to http://127.0.0.1:8000/admin/ and login with username: **admin** and password: **admin**.

## TODO

- make pip installable
- make installation simple by adding app to INSTALLED_APPS, MIDDLEWARE_CLASSES, or similar
- add "404 Not Found" destination
- add exact match to permanent redirect 301
- add exact match to temporary redirect 302
- add regex match to permanent redirect 301
- add regex match to temporary redirect 302
- add regex match to include (e.g. add the ability to use a destination like include('django.contrib.admindocs.urls'))
- add unit tests (relative redirect, absolute redirect, regex match, 404, etc.)

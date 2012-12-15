django-urls
===========

Manage URL Patterns and Views via the Django admin.

## Screenshots

![django-urls screenshot](https://raw.github.com/django-urls/django-urls/master/screenshot.png "")

## Requirements

* Django `1.4.x`.

## Installation

Add both **django_urls** and **news** to `INSTALLED_APPS` in `settings.py`.

    INSTALLED_APPS = (
        # ...
        'django_urls',
        'news',
    )

And add django_urls to `urls.py`.

    from django_urls import django_urls
    urlpatterns += django_urls()

## TODO / Pull Requests Wanted

- <del>make pip installable</del>
- <del>make installation simple by adding app to INSTALLED_APPS, MIDDLEWARE_CLASSES, or similar</del>
- add "404 Not Found" destination
- add exact match to permanent redirect 301
- add exact match to temporary redirect 302
- add regex match to permanent redirect 301
- add regex match to temporary redirect 302
- add regex match to include (e.g. add the ability to use a destination like include('django.contrib.admindocs.urls'))
- add unit tests (relative redirect, absolute redirect, regex match, 404, etc.)

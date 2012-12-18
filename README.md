django-urls
===========

Manage URL Patterns and Views via the Django admin.

## Screenshots

![django-urls screenshot](https://raw.github.com/django-urls/django-urls/master/screenshot.png "")

## Requirements

* Django `1.4.x`.

## Installation

1. Install django-urls.

        pip install -e git+git://github.com/django-urls/django-urls.git#egg=django_urls

2. Add **django_urls** to `INSTALLED_APPS` in `settings.py`.

        INSTALLED_APPS = (
            # ...
            'django_urls',
            # ...
        )

3. Add django_urls to `urls.py`.

        from django_urls import django_urls
        urlpatterns += django_urls()

## TODO / Pull Requests Wanted

- <del>make pip installable</del>
- <del>make installation simple by adding app to INSTALLED_APPS, MIDDLEWARE_CLASSES, or similar</del>
- add "404 Not Found" destination
- <del>add exact match to permanent redirect 301</del>
- <del>add exact match to temporary redirect 302</del>
- <del>add regex match to permanent redirect 301</del>
- <del>add regex match to temporary redirect 302</del>
- add regex match to include (e.g. add the ability to use a destination like include('django.contrib.admindocs.urls'))
- add unit tests (relative redirect, absolute redirect, regex match, 404, etc.)
- add Url.order as "Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL."
- add file editing for destination views using a modal and [ajaxorg/ace](https://github.com/ajaxorg/ace)
- add ability to save urls to file (e.g. python manage.py dumpdata django_urls --indent=4)

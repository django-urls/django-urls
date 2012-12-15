Example News Project using django-urls
======================================

In this example, both **django_urls** and **news** are added to `INSTALLED_APPS` in [`settings.py`](/django-urls/django-urls/blob/master/example/news/settings.py).

    INSTALLED_APPS = (
        # ...
        'django_urls',
        'news',
    )

Also, django_urls is added to [`urls.py`](/django-urls/django-urls/blob/master/example/news/urls.py).

    from django_urls import django_urls
    urlpatterns += django_urls()

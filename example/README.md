Example News Project using django-urls
======================================

## Run the Example Demo

    mkdir --parents ~/Projects
    cd ~/Projects
    git clone https://github.com/django-urls/django-urls.git django-urls
    cd django-urls/example
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv django-urls
    pip install --requirement requirements.txt
    python manage.py syncdb --noinput
    python manage.py runserver

Go to http://127.0.0.1:8000/admin/ and login with username: **admin** and password: **admin**.

## Installation

In this example, both **django_urls** and **news** are added to `INSTALLED_APPS` in [`settings.py`](/django-urls/django-urls/blob/master/example/news/settings.py).

    INSTALLED_APPS = (
        # ...
        'django_urls',
        'news',
    )

Also, django_urls is added to [`urls.py`](/django-urls/django-urls/blob/master/example/news/urls.py).

    from django_urls import django_urls
    urlpatterns += django_urls()

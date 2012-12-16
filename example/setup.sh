#!/bin/bash

set -x

mkdir --parents ~/Projects
cd ~/Projects
git clone https://github.com/django-urls/django-urls.git django-urls
cd django-urls/example
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv django-urls
pip install django
pip install -e git+git://github.com/django-urls/django-urls.git#egg=django_urls
python manage.py syncdb --noinput
python manage.py runserver

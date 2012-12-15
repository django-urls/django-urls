from django.conf.urls import include, patterns, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'url.views.home', name='home'),
    # url(r'^url/', include('url.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from url import django_urls
urlpatterns += django_urls()

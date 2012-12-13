from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic import RedirectView

from url.models import Url


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'url.views.home', name='home'),
    # url(r'^url/', include('url.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

url_list = Url.objects.filter(enabled=True)

for the_url in url_list:
    regex = the_url.url
    type = the_url.type
    view = the_url.destination

    if type == 'exact_to_redirect':
        regex = r'^{0}$'.format(regex)
        # URI scheme check
        if not '://' in view:
            # relative redirect
            view = '/{0}'.format(view)
        urlpatterns += patterns('', url(regex, RedirectView.as_view(url=view, permanent=False)),)
    elif type == 'exact_to_view':
        regex = r'^{0}$'.format(regex)
        urlpatterns += patterns('', url(regex, view),)
    elif type == 'regex_to_redirect':
        # URI scheme check
        if not '://' in view:
            # relative redirect
            view = '/{0}'.format(view)
        urlpatterns += patterns('', url(regex, RedirectView.as_view(url=view, permanent=False)),)
    elif type == 'regex_to_view':
        urlpatterns += patterns('', url(regex, view),)
    else:
        continue


# TODO: Make install simple; e.g.:
# from django_urls import django_urls
# urlpatterns += django_urls()

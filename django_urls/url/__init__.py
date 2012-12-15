from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from url.models import Url


def django_urls():
    urlpatterns = []
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

    return urlpatterns

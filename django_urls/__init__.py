from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from models import Url

__all__ = ['django_urls',]


def django_urls():
    urlpatterns = []
    url_list = Url.objects.filter(enabled=True)

    for the_url in url_list:
        regex = the_url.url
        type = the_url.type
        view = the_url.destination

        # Exact matches
        if type in ['exact_to_view',
                    'exact_to_temporary_redirect',
                    'exact_to_permanent_redirect',]:
            regex = r'^{0}$'.format(regex)

        # Views
        if type in ['regex_to_view', 'exact_to_view',]:
            urlpatterns += patterns('', url(regex, view),)
        # Redirects
        elif type in ['regex_to_temporary_redirect', 'regex_to_permanent_redirect',
                      'exact_to_temporary_redirect', 'exact_to_permanent_redirect',]:
            permanent = False
            if type in ['regex_to_permanent_redirect', 'exact_to_permanent_redirect',]:
                permanent = True
            # Make url relative if needed by checking URI scheme
            if not '://' in view:
                view = '/{0}'.format(view)
            urlpatterns += patterns('', url(regex, RedirectView.as_view(url=view, permanent=permanent)),)
        else:
            continue

    return urlpatterns

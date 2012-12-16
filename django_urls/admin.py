import re

from django.contrib import admin
from django.template.defaultfilters import escape

from models import Url


class UrlAdmin(admin.ModelAdmin):
    def url_column(self):
        if self.type in ['exact_to_view', 'exact_to_temporary_redirect', 'exact_to_permanent_redirect',]:
            column = '<pre><span>^</span>{0}<span>$</span></pre>'.format(escape(self.url))
        elif self.type in ['regex_to_view', 'regex_to_temporary_redirect', 'regex_to_permanent_redirect',]:
            column = '<pre class="regex">{0}</pre>'.format(escape(self.url))
        else:
            column = '<pre>{0}</pre>'.format(self.url)
        return column
    url_column.short_description = 'URL'
    url_column.allow_tags = True

    def destination_column(self):

        if self.type in ['regex_to_temporary_redirect', 'regex_to_permanent_redirect',
                         'exact_to_temporary_redirect', 'exact_to_permanent_redirect',]:
            # Make url relative if needed by checking URI scheme
            if not '://' in self.destination:
                destination_href = '/{0}'.format(self.destination)
                destination_text = '<span>/</span>{0}'.format(self.destination)
            else:
                destination_href = self.destination
                destination_text = self.destination
            column = '<pre><a href="{0}" target="_blank">{1}</a></pre>'.format(destination_href,
                                                                               destination_text)
        elif self.type in ['regex_to_view', 'exact_to_view',]:
            param_list = re.findall(r'\(\?P<(.*?)>.*?\)', self.url)
            column = '<pre>{0}({1})</pre>'.format(self.destination, ', '.join(param_list))
        else:
            column = self.destination
        return column
    destination_column.allow_tags = True
    destination_column.short_description = 'Destination'

    list_display = ('pk', url_column, 'type', destination_column, 'enabled',)

    class Media:
        css = {
            'all': (
                #'css/default.css',
                'css/nobg.css',
                #'css/regexpal.css',
                #'css/regexbuddy.css',
                'css/regex.css',
            )
        }
        js = (
            'js/regex-colorizer.js',
            'js/regex-init.js',
        )

admin.site.register(Url, UrlAdmin)

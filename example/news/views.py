from django.http import HttpResponse


def robots(request):
    return HttpResponse(('User-agent: *\n'
        'Disallow: '), content_type='text/plain')


def special_case_2003(request):
    return HttpResponse('OK', content_type='text/plain')


def year_archive(request, year):
    return HttpResponse('OK', content_type='text/plain')


def month_archive(request, year, month):
    return HttpResponse('OK', content_type='text/plain')


def article_detail(request, year, month, day):
    return HttpResponse('OK', content_type='text/plain')

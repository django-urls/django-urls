from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=255)
    TYPE_CHOICES = (
        ('regex_to_view',               'Regex match to view'),
        ('regex_to_temporary_redirect', 'Regex match to temporary redirect'),
        ('regex_to_permanent_redirect', 'Regex match to permanent redirect'),
        ('exact_to_view',               'Exact match to view'),
        ('exact_to_temporary_redirect', 'Exact match to temporary redirect'),
        ('exact_to_permanent_redirect', 'Exact match to permanent redirect'),
    )
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='exact_to_view')
    destination = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)

    # TODO: Add Url.order as "Django runs through each URL pattern, in order,
    # and stops at the first one that matches the requested URL." and set
    # Url.Meta.ordering = ['order',]

    class Meta:
        ordering = ['pk',]

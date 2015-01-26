from django.contrib.sitemaps import Sitemap
from Union_1.models import Event
import datetime


class EventSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return 'event/desert/'


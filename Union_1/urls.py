__author__ = 'Sylvestre'

from django.conf.urls import patterns, url
from django.contrib.sitemaps import GenericSitemap

from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

from Union_1.models import Event,Picture
from Union_1 import views

event_dict = {
    'queryset': Event.objects.all(),
}

class ViewSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['index', 'event_home', 'become_a_member', 'become_a_member_form','become_a_friend','membership_renewal','contact_us','contact_us_thank_you','gallery','membership_payment']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'event': GenericSitemap(event_dict, priority=0.6),
    'views': ViewSitemap
    #'picture': GenericSitemap(picture_dict, priority=0.6),
}

urlpatterns = patterns('',
        url(r'^$',views.index,name='index'),
        url(r'^blog/(?P<blog_title_url>\w+)$', views.blog,name='blog'),
        url(r'^blog/',views.blog_home,name='blog_home'),
        url(r'^events/(?P<event_title_url>\w+)/', views.event_detail,name='event'),
        url(r'^event/',views.event,name='event_home'),
        url(r'^about-us/',views.about,name='about'),
        url(r'^members/',views.membership,name='become_a_member'),
        url(r'^membership/become_a_member/$',views.membership_become_member,name='become_a_member_form'),
        url(r'^membership/become_a_friend/$',views.membership_become_a_friend,name='become_a_friend'),
        url(r'^membership/renewal/$',views.renewal,name='membership_renewal'),
        url(r'^contact_us/',views.contact_us,name='contact_us'),
        url(r'^contact_us_thank_you/',views.contact_us_thank_you,name='contact_us_thank_you'),
        #url(r'^gallery/$',views.gallery,name='gallery'),
        url(r'^membership/payment',views.membership_payment,name='membership_payment'),
        (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
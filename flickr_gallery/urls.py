__author__ = 'Sylvestre'

from django.conf.urls import patterns, url
from django.contrib.sitemaps import GenericSitemap

from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

from flickr_gallery import views

urlpatterns = patterns('',
        url(r'^gallery/$',views.gallery,name='gallery'),
)
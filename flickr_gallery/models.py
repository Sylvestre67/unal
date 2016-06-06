from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

class FlickR_Album(models.Model):
    name = models.CharField(max_length=256,null=True,blank=True)
    flickr_id = models.CharField(max_length=256,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(null=True,blank=True)
    photo_feed = JSONField(null=True,blank=True)

    def __unicode__(self):
        return self.name
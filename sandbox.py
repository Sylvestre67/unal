__author__ = 'Sylvestre'
import os
from django.template import RequestContext
from Union_1.models import Event,BlogPost,Contact_Us,Picture,Album

def find_foregin_key(object,name):
    c = object.objects.get_or_create(name=name)
    print c.key

find_foregin_key(Album,'Random pictures')
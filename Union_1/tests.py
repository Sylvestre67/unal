"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ua_67.settings'
from django.test import TestCase
from Union_1.models import Member,Event

def get_event():
        c= Event.objects.all()
        return c

print ('we are testing!')
get_event()

class SimpleTest(TestCase):
    def get_event(self):
        c= Event.objects.all()
        return c



get_event()


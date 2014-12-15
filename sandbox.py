__author__ = 'Sylvestre'
import datetime
import mailchimp
from django.template import RequestContext
from Union_1.models import Event,BlogPost,Contact_Us,Picture

from mailchimp import utils

date = datetime.datetime(2012,2,3,18,30)
print (date)

list = mailchimp.utils.get_connection().get_list_by_id('7366bb50d3')

def gallery(request):

    events = Event.objects.prefetch_related('picture_set').all()
    images = Picture.objects.all()

    print(events)
    print(images)
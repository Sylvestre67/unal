__author__ = 'Sylvestre'

import os
import django
from django.core.wsgi import get_wsgi_application

def get_event():
    c=Event.objects.all()
    return c

if __name__ == '__main__':
    django.setup()
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ua_67.settings'
    application = get_wsgi_application()
    from Union_1.models import Member,Event
    get_event()
    print('Hello World!')
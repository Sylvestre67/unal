__author__ = 'Sylvestre'

import os
import datetime

def populate():

    add_event(title='Alsace Brooklyn Party',date=datetime.datetime(2015,01,10,20,30),price=0,url='http://www.google.com',place='123 45th street, New York City',description='Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit. Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit',bwp_link="http://www.brownpapertickets.com/event/964609",venue="La Cigogne")
    add_event(title='Christmas Party',date=datetime.datetime(2014,12,06,18,30),price=59,url='http://www.google.com',place='123 45th street, New York City',description='Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit. Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit',bwp_link="",venue="")
    add_event(title='Union Alsacienne Garden Party',date=datetime.datetime(2014,8,10,14,30),price=45,url='http://www.google.com',place='123 45th street, New York City',description='Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit. Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit',bwp_link="",venue="")

    add_contact_us(subject='TEST-EMAIL',message='1231321321',sender='g@g.com',cc='True')

    add_album(name='Random pictures')

    add_picture(name='TEST',picture='images/UA_Spring_Potluck.jpg')
    add_picture(name='Christmas Drink',picture='images/Union-Alsacienne-05.jpg')
    add_picture(name='Christmas Couple',picture='images/Union-Alsacienne-12.jpg')
    add_picture(name='Alsace in Brooklyn',picture='images/Union-Alsacienne-23.jpg')

def add_BlogPost(title,body):
    b = BlogPost.objects.get_or_create(title=title,body=body)
    return b

def add_picture(name,picture):
    p = Picture.objects.get_or_create(name=name,picture=picture)
    return p

def add_event(title,date,price,url,place,description,bwp_link,venue):
    e = Event.objects.get_or_create(title=title,date=date,price=price,url=url,place=place,description=description,bwp_link=bwp_link,venue=venue)
    return e

def add_album(name):
    a = Album.objects.get_or_create(name=name)
    return a

def add_contact_us(subject,message,sender,cc):
    c = Contact_Us.objects.get_or_create(subject=subject,message=message,sender=sender,cc=cc)
    return c

if __name__ == '__main__':
    print 'Let\'s populate Union_1'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ua_67.settings')
    from Union_1.models import BlogPost,Event,Contact_Us,Album,Picture
    populate()


__author__ = 'Sylvestre'

import os
import datetime

def populate():
    add_BlogPost(title='1 Test Alsace',
                              body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit.'
    )

    add_BlogPost(title='2 Test Alsace',
                              body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit.'
    )

    add_BlogPost(title='3 Test Alsace',
                              body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit.'
    )

    add_BlogPost(title='4 Test Alsace',
                              body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit.'
    )

    add_BlogPost(title='5 Test Alsace',
                              body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit.'
    )

    add_BlogPost(title='6 Test Alsace',
                              body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisi nisl, tristique id ornare sit amet, consequat a erat. Etiam a vehicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vitae, ultrices tortor. Mauris pellentesque risus dui, non pellentesque ex egestas in. Nullam suscipit massa justo. In sit amet magna eget velit tristique sagittis at vitae arcu. Donec ullamcorper sed lorem vitae blandit.'
    )

    add_event(title='Alsace Brooklyn Party',date=datetime.datetime(2015,01,10,20,30),price=0,url='http://www.google.com',place='123 45th street, New York City',description='Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit. Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit',bwp_link="http://www.brownpapertickets.com/event/964609",venue="La Cigogne")
    add_event(title='Christmas Party',date=datetime.datetime(2014,12,06,18,30),price=59,url='http://www.google.com',place='123 45th street, New York City',description='Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit. Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit',bwp_link="",venue="")
    add_event(title='Union Alsacienne Garden Party',date=datetime.datetime(2014,8,10,14,30),price=45,url='http://www.google.com',place='123 45th street, New York City',description='Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit. Dolor sit ame odio laoreethicula elit, non vehicula magna. Proin quis dolor odio. Sed et auctor arcu. Donec tempor ultrices hendrerit. Sed nec odio laoreet, pulvinar neque vit',bwp_link="",venue="")

    add_contact_us(subject='TEST-EMAIL',message='1231321321',sender='g@g.com',cc='True')

def add_BlogPost(title,body):
    b = BlogPost.objects.get_or_create(title=title,body=body)
    return b

def add_event(title,date,price,url,place,description,bwp_link,venue):
    e = Event.objects.get_or_create(title=title,date=date,price=price,url=url,place=place,description=description,bwp_link=bwp_link,venue=venue)
    return e

def add_contact_us(subject,message,sender,cc):
    c = Contact_Us.objects.get_or_create(subject=subject,message=message,sender=sender,cc=cc)
    return c

if __name__ == '__main__':
    print 'Let\'s populate Union_1'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ua_67.settings')
    from Union_1.models import BlogPost,Event,Contact_Us
    populate()


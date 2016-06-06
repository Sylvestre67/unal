# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from django.core.exceptions import ObjectDoesNotExist

from cloudinary import CloudinaryImage
from postmark import PMMail

from django.views.decorators.cache import cache_page

from models import Event,BlogPost,Contact_Us,Picture,Album,BureauMember,FlickR_Album
from forms import ContactUs_Form,Become_a_Member,Become_a_Friend,Renewal

import datetime

def encode_url(name):
    name_url = name.replace(' ','_')
    return name_url

def decode_url(name_url):
    name = name_url.replace('_',' ')
    return name

def encode_query_for_google_direction_url(direction):
    google_url_direction=(((direction.replace(' ','+')).replace(',','')).replace('.',''))
    return google_url_direction

def index(request):
    context = RequestContext(request)
    now = datetime.date.today()

    event_list = Event.objects.filter(date__gte=now).order_by('date')

    for e in event_list:
        e.url_link = encode_url(e.title)

    for e in event_list:
        e.google_direction = encode_query_for_google_direction_url(e.address)

    context_dict = {'event_list' : event_list}

    return render_to_response('Union_1/index.html',context_dict,context)

def blog(request, blog_title_url):
    context = RequestContext(request)
    blog_title = decode_url(blog_title_url)

    blogpost_list = BlogPost.objects.order_by('-title')
    context_dict = {'blog_title': blog_title, 'blogposts': blogpost_list,'blog_title_url':blog_title_url}

    for b in blogpost_list:
        b.url = encode_url(b.title)

    try:
        blog = BlogPost.objects.get(title=blog_title)
        context_dict['blog'] = blog
    except BlogPost.DoesNotExist:
        pass

    return render_to_response('Union_1/blog.html', context_dict,context)

def blog_home(request):
    context = RequestContext(request)
    blogpost_list = BlogPost.objects.order_by('-title')

    context_dict = {'blogposts': blogpost_list}

    for b in blogpost_list:
        b.url = encode_url(b.title)

    return render_to_response('Union_1/blog_home.html',context_dict,context)

def event(request):
    context = RequestContext(request)
    event_list = Event.objects.exclude(date__lt= datetime.datetime.now()).order_by('date')
    event_list_past = Event.objects.exclude(date__gt= datetime.datetime.now()).order_by('-date')[:5]

    for e in event_list:
        e.url_link = encode_url(e.title)

    for e in event_list:
        e.google_direction = encode_query_for_google_direction_url(e.address)

    for e in event_list_past:
        e.url_link = encode_url(e.title)

    for e in event_list_past:
        e.google_direction = encode_query_for_google_direction_url(e.address)

    context_dict = {'event_list' : event_list, 'event_past' : event_list_past }

    return render_to_response('Union_1/Event_List.html',context_dict,context)

def event_detail(request,event_title_url):
    context=RequestContext(request)
    event_title=decode_url(event_title_url)

    event_list=Event.objects.order_by('-date')
    context_dict = {'event_title' : event_title,'event_list' : event_list, 'event_title_url' : event_title_url }

    for e in event_list:
        e.url_link = encode_url(e.title)
        e.google_direction = encode_query_for_google_direction_url(e.address)

        try:
            event = Event.objects.get(title=event_title)
            event.google_direction = encode_query_for_google_direction_url(event.address)
            event.url_link_og = encode_url(event.title)
            context_dict['event'] = event
        except Event.DoesNotExist:
            pass

    return render_to_response('Union_1/Event.html',context_dict,context)

def about(request):

    context=RequestContext(request)
    bureau_member=BureauMember.objects.order_by('list_position')

    context_dict={"bureau_member" : bureau_member}
    return render_to_response('Union_1/about.html',context_dict,context)

def membership_become_member(request):

    context=RequestContext(request)

    if request.method == 'POST':
        form = Become_a_Member(request.POST)

        if form.is_valid():

            subject='New Member Application Received'
            message= ("A new request for membership has been posted through l'Union Alsacienne Website." + "\r\n\n" +
            "Name: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] + "\r\n" +
            "Address: " + form.cleaned_data['address'] + "\n" +
            form.cleaned_data['city'] + "   " + form.cleaned_data['zip'] + "   " + form.cleaned_data['state'] + "\r\n\n" +
            "Occupation: " + form.cleaned_data['occupation'] + "\n" + " at " + form.cleaned_data['company'] + "\r\n\n" +
            "Mobile phone: " + form.cleaned_data['mobile_phone'] + "\n" + " Home phone: " + form.cleaned_data['home_phone'] + "\n" +
            " Fax: " + form.cleaned_data['home_fax'] + "\r\n\n" +
            "E-mail: " + form.cleaned_data['email'] + "\r\n\n" + "Date of birth: " + str(form.cleaned_data['date_of_birth']) + "\n" +
            "Place: " + form.cleaned_data['birth_place'] + "\n" +
            "If not from Alsace: " + form.cleaned_data['if_not_alsace_Reason'] + "\r\n\n" +
            "Venue: " + form.cleaned_data['venue'] + "\n" + "Date: " + str(form.cleaned_data['date_membership_application']) + "\n" +
            "Signature: " + form.cleaned_data['signature'] + "\r\n\n" +
            "First sponsor: " + form.cleaned_data['first_sponsor'] + "\n" +
            "Second sponsor: " + form.cleaned_data['second_sponsor'] + "\r\n\n" + "Posted through l'Union Alsacienne Website"+ "\r\n")
            recipient=['contact@alsace-newyork.com','sgug@outlook.com','treasury.unal@gmail.com']

            email = PMMail(subjet = subject,
                         text_body = message,
                         to = recipient)
            email.send()

            msg_body =  (
                    "Dear " + form.cleaned_data['first_name'] + "\r\n\n" +
                    "Thank you for your request of membership. Here's the information you submitted."+ "\n\n" +
                     "Name: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] +"\n\n" +
                     "Email: " + form.cleaned_data['email'] + "\n\n" +
                     "Address: " + form.cleaned_data['address'] + "\n" +
                     form.cleaned_data['city'] + "   " + form.cleaned_data['zip'] + "   " + form.cleaned_data['state'] + "\r\n\n" +
                     "If you choose to pay your fee by check, please mail your check to: " +"\r\n"+
                     "Union Alsacienne of New York - Mrs. Andrea Markson"+ "\r\n"+
                     "240 76th street - Apt. 3H"+ "\r\n"+
                     "New York, NY - 10021"+ "\r\n\n"+
                     "Best,"+ "\r\n\n"+
                     "L'Union of Alsacienne of New York. "+ "\r\n"
            )

            msg = PMMail(subject = "Thank you for your application",
                         text_body = msg_body,
                         to = form.cleaned_data['email'])

            msg.send()

            form.save(True)

            return HttpResponseRedirect('/membership/payment?type=1') #redirect after post

        else:
            print form.errors
    else:
        form = Become_a_Member()

    return render_to_response('Union_1/become_a_member.html',{'form':form},context)

def membership_payment(request):
    context=RequestContext(request)

    event_list = Event.objects.order_by('-date')

    for e in event_list:
        e.when = datetime.date((e.date).year,(e.date).month,(e.date).day)
        e.today = datetime.date.today()
        if e.when > e.today:
            e.comp = 'upcoming'
        if e.when < e.today:
             e.comp = 'past'
        if e.when == e.today:
             e.comp = 'today'

    for e in event_list:
        e.url_link = encode_url(e.title)

    context_dict = {'event_list' : event_list}

    return render_to_response('Union_1/members_payment.html',context_dict,context)

def membership_become_a_friend(request):
    context=RequestContext(request)

    if request.method =='POST':
        form = Become_a_Friend(request.POST)

        if form.is_valid():

            subject = 'New Friendship Application Received'
            message = ( "A new request to become a friend has been posted through l'Union Alsacienne Website"+ "\n\n" +
                        "Name: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] +"\n\n" +
                        "Email: " + form.cleaned_data['email'] + "\n\n" +
                        "Address: " + form.cleaned_data['address'] + "\n" +
                        form.cleaned_data['city'] + "   " + form.cleaned_data['zip'] + "   " + form.cleaned_data['state'] + "\r\n\n" +
                        "Posted through l'Union Alsacienne Website"+ "\r\n")

            recipient =  'contact@alsace-newyork.com,sgug@outlook.com,treasury.unal@gmail.com'

            email = PMMail(subject = subject,
                           text_body = message,
                           to = recipient,
                           tag = 'member_form')
            email.send()

            external_subject = 'Thank you for your application'
            external_message = (
                    "Dear " + form.cleaned_data['first_name'] + "\r\n\n" +
                    "Thank you for your friendship. Here's the information you submitted."+ "\n\n" +
                     "Name: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] +"\n\n" +
                     "Email: " + form.cleaned_data['email'] + "\n\n" +
                     "Address: " + form.cleaned_data['address'] + "\n" +
                     form.cleaned_data['city'] + "   " + form.cleaned_data['zip'] + "   " + form.cleaned_data['state'] + "\r\n\n" +
                     "If you choose to pay your fee by check, please mail your check to: " +"\r\n"+
                     "Union Alsacienne of New York - Mrs. Andrea Markson"+ "\r\n"+
                     "240 76th street - Apt. 3H"+ "\r\n"+
                     "New York, NY - 10021"+ "\r\n\n"+
                     "Best,"+ "\r\n\n"+
                     "L'Union of Alsacienne of New York. "+ "\r\n"
            )
            external_recipient = form.cleaned_data['email']

            external_email = PMMail(subject = external_subject,
                           text_body = external_message,
                           to = external_recipient,
                           tag = 'member_form')

            external_email.send()

            form.save(True)

            return HttpResponseRedirect('/membership/payment?type=2')
        else:
            print form.errors
    else:
        form = Become_a_Friend()

    return render_to_response('Union_1/become_a_friend.html',{'form':form},context)

def renewal(request):
    context=RequestContext(request)

    if request.method =='POST':
        form = Renewal(request.POST)

        if form.is_valid():

            internal_subject='Renewal of Membership/Friendship received'
            internal_message=("This Member renewed its Membership/Friendship through l'Union Alsacienne Website"+ "\n\n" +
                     "Name: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] +"\n\n" +
                     "Email: " + form.cleaned_data['email'] + "\n\n" +
                     "Address: " + form.cleaned_data['address'] + "\n" +
                     form.cleaned_data['city'] + "   " + form.cleaned_data['zip'] + "   " + form.cleaned_data['state'] + "\r\n\n" +
                     "Posted through l'Union Alsacienne Website"+ "\r\n")
            internal_recipient= 'contact@alsace-newyork.com,sgug@outlook.com,treasury.unal@gmail.com'

            internal_email = PMMail(subject = internal_subject,
                           text_body = internal_message,
                           to = internal_recipient,
                           tag = 'renewal_form')

            internal_email.send()

            external_subject='Thank you for your renewal!'
            external_message=(
                    "Dear " + form.cleaned_data['first_name'] + "\r\n\n" +
                    "Thank you for your renewal. Here's the information you submitted."+ "\n\n" +
                     "Name: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] +"\n\n" +
                     "Email: " + form.cleaned_data['email'] + "\n\n" +
                     "Address: " + form.cleaned_data['address'] + "\n" +
                     form.cleaned_data['city'] + "   " + form.cleaned_data['zip'] + "   " + form.cleaned_data['state'] + "\r\n\n" +
                     "If you choose to pay your fee by check, please mail your check to: " +"\r\n"+
                     "Union Alsacienne of New York - Mrs. Andrea Markson"+ "\r\n"+
                     "240 76th street - Apt. 3H"+ "\r\n"+
                     "New York, NY - 10021"+ "\r\n\n"+
                     "Best,"+ "\r\n\n"+
                     "L'Union of Alsacienne of New York. "+ "\r\n"
            )

            external_recipient= form.cleaned_data['email']

            external_email = PMMail(subject = external_subject,
                           text_body = external_message,
                           to = external_recipient,
                           tag = 'renewal_form')

            external_email.send()

            if form.cleaned_data['member_type'] == 'F':
                return HttpResponseRedirect('/membership/payment?type=2&action=renewal')
            else:
                return HttpResponseRedirect('/membership/payment?type=1&action=renewal')
        else:
            print form.errors
    else:
        form = Renewal()

    return render_to_response('Union_1/renewal.html',{'form':form},context)

def membership(request):
    context=RequestContext(request)
    event_list = Event.objects.order_by('-date')

    for e in event_list:
        e.when = datetime.date((e.date).year,(e.date).month,(e.date).day)
        e.today = datetime.date.today()
        if e.when > e.today:
            e.comp = 'upcoming'
        if e.when < e.today:
             e.comp = 'past'
        if e.when == e.today:
             e.comp = 'today'

    for e in event_list:
        e.url_link = encode_url(e.title)

    context_dict = {'event_list' : event_list}

    return render_to_response('Union_1/membership.html',context_dict,context)

def contact_us(request):
    context=RequestContext(request)
    mail_list = Contact_Us.objects.order_by('-date')

    if request.method == 'POST':
        form = ContactUs_Form(request.POST)

        if form.is_valid():

            subject=form.cleaned_data['subject']

            message=("From: " + form.cleaned_data['sender'] +"\r\n" +
            "Subject: " + form.cleaned_data['subject'] + "\r\n"
            "Message: " + form.cleaned_data['message'] + "\r\n\n" + "Posted through l'Union Alsacienne Website"+ "\r\n" )

            sender=form.cleaned_data['sender']
            cc_myself=form.cleaned_data['cc']

            #recipients='contact@alsace-newyork.com,sgug@outlook.com'

            recipients='union@alsace.nyc'

            if cc_myself:
                recipients = recipients + ',' + sender

            email = PMMail(subject = subject,
                           text_body = message,
                           to = recipients,
                           tag = 'contact_form')
            email.send()

            form.save(True)

            return HttpResponseRedirect('/contact_us_thank_you/') #redirect after post

        else:
            print form.errors
    else:
        form = ContactUs_Form()

    return render_to_response('Union_1/contact_us.html',{'form':form,'mail_list':mail_list},context)

def contact_us_thank_you(request):
    context= RequestContext(request)
    return render_to_response('Union_1/contact_thanks.html',context)


from ua_67.settings import FLICKR_API_KEY,FLICKR_SECRET,FLICKR_USERID
import flickrapi
import json
import yaml

@cache_page(60 * 60 * 24)
def gallery(request):
        context= RequestContext(request)

        flickr = flickrapi.FlickrAPI(FLICKR_API_KEY,FLICKR_SECRET,format='parsed-json')
        sets = flickr.photosets.getList(user_id=FLICKR_USERID)

        for album in sets['photosets']['photoset']:
            try:
                existing_album = FlickR_Album.objects.get(flickr_id = album['id'])
                """
                try:
                    photo_feed = flickr.photosets.getPhotos(user_id=FLICKR_USERID,photoset_id=existing_album.flickr_id)

                    existing_album.photo_feed = yaml.safe_load(json.dumps(photo_feed))
                    existing_album.save()

                except Exception as e:
                    pass
                """
            except ObjectDoesNotExist:
                new_album = FlickR_Album.objects.create(name=album['title']['_content'],flickr_id=album['id'])
                try:
                    photo_feed = flickr.photosets.getPhotos(user_id=FLICKR_USERID,photoset_id=new_album.flickr_id)

                    new_album.photo_feed = yaml.safe_load(json.dumps(photo_feed))
                    new_album.save()

                except Exception as e:
                    print(e)

        albums_for_template = FlickR_Album.objects.all()
        context_dict = {'albums' : albums_for_template}

        return render_to_response('Union_1/gallery.html', context_dict, context)



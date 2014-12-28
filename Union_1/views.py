# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from Union_1.models import Event,BlogPost,Contact_Us,Picture,Album
from forms import ContactUs_Form,Become_a_Member,Become_a_Friend,mailchimp_form
from django.core.mail import send_mail
from mailchimp import utils

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

    blogpost_list = BlogPost.objects.order_by('-title')[:5]
    event_list = Event.objects.order_by('date')

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

    for e in event_list:
        e.google_direction = encode_query_for_google_direction_url(e.place)

    for b in blogpost_list:
        b.url = encode_url(b.title)

    context_dict = {'blogpost_list': blogpost_list,'event_list' : event_list}

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
    event_list = Event.objects.prefetch_related('picture_set').all().order_by('date')

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

    for e in event_list:
        e.google_direction = encode_query_for_google_direction_url(e.place)

    context_dict = {'event_list' : event_list}

    return render_to_response('Union_1/Event_List.html',context_dict,context)

def event_detail(request,event_title_url):
    context=RequestContext(request)
    event_title=decode_url(event_title_url)

    event_list=Event.objects.order_by('-date')
    context_dict = {'event_title' : event_title,'event_list' : event_list, 'event_title_url' : event_title_url }

    for e in event_list:
        e.url_link = encode_url(e.title)
        e.google_direction = encode_query_for_google_direction_url(e.place)

        try:
            event = Event.objects.get(title=event_title)
            event.google_direction = encode_query_for_google_direction_url(event.place)
            context_dict['event'] = event
        except Event.DoesNotExist:
            pass

    return render_to_response('Union_1/Event.html',context_dict,context)

def about(request):
    return render_to_response('Union_1/about.html')

def membership_become_member(request):

    context=RequestContext(request)

    if request.method == 'POST':
        form = Become_a_Member(request.POST)

        if form.is_valid():
            subject='New Friend Apllication Recieved'
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
            " Signature: " + form.cleaned_data['signature'] + "\r\n\n" +
            "First sponsor: " + form.cleaned_data['first_sponsor'] + "\n" +
            "Second sponsor: " + form.cleaned_data['second_sponsor'] + "\r\n\n" + "Posted through l'Union Alsacienne Website"+ "\r\n")
            sender='website@alsace.nyc'
            recipient=['sgug@outlook.com',form.cleaned_data['email']]

            send_mail(subject,message,sender,recipient,fail_silently=False)

            form.save(True)

            return HttpResponseRedirect('/') #redirect after post

        else:
            print form.errors
    else:
        form = Become_a_Member()

    return render_to_response('Union_1/become_a_member.html',{'form':form},context)

def membership_become_a_friend(request):
    context=RequestContext(request)

    if request.method =='POST':
        form = Become_a_Friend(request.POST)

        if form.is_valid():
            subject='New Friend Apllication Recieved'
            message=("A new request to become a friend has been posted through l'Union Alsacienne Website"+ "\n\n" +
                     "Name: " + form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'] +"\n\n" +
                     "Email: " + form.cleaned_data['email'] + "\n\n" +
                     "Address: " + form.cleaned_data['address'] + "\n" +
                     form.cleaned_data['city'] + "   " + form.cleaned_data['zip'] + "   " + form.cleaned_data['state'] + "\r\n\n" +
                     "Posted through l'Union Alsacienne Website"+ "\r\n")
            sender='website@alsace.nyc'
            recipient=['sgug@outlook.com',form.cleaned_data['email']]

            send_mail(subject,message,sender,recipient,fail_silently=False)

            form.save(True)

            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = Become_a_Friend()

    return render_to_response('Union_1/become_a_friend.html',{'form':form},context)

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

            recipients=['sgug@outlook.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject,message,sender,recipients, fail_silently=False)

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

def mailchimp(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = mailchimp_form(request.POST)


        if form.is_valid():
            list = utils.get_connection().get_list_by_id('7366bb50d3')
            list.subscribe(form.cleaned_data['email'], {'EMAIL': form.cleaned_data['email']})
            return HttpResponseRedirect('/union/')
        else:
            print form.errors
    else:
        form = mailchimp_form()

    return render_to_response('Union_1/sign_up.html',{'form':form},context)


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def gallery(request):
    context= RequestContext(request)
    events = Event.objects.prefetch_related('picture_set').filter(picture__event__isnull=False).order_by('-date')

    paginator = Paginator(events, 4)
    number = paginator.page_range

    page = request.GET.get('page')
    try:
        event_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        event_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        event_page = paginator.page(paginator.num_pages)

    albums = Album.objects.prefetch_related('picture_set').all()

    context_dict = {'events' : events,'albums' : albums, 'event_page': event_page,'number' : number}
    return render_to_response('Union_1/gallery.html',context_dict,context)


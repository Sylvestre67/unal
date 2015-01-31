from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

def encode_url(name):
    name_url = name.replace(' ','_')
    return name_url

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body= models.TextField(max_length=80000)

    def __unicode__(self):
        return self.title

class Event(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateTimeField(blank=True)
    price=models.CharField(max_length=50)
    url=models.URLField(blank=True)
    address=models.CharField(max_length=4000)
    venue=models.CharField(max_length=4000)
    description=models.TextField(max_length=80000,blank=True)
    bwp_link=models.URLField(blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_title_url':encode_url(self.title)})

class EventAdmin(admin.ModelAdmin):
    search_fields = ["date"]
    list_display = ["date","title","description"]

class Contact_Us(models.Model):

    subject=models.CharField(max_length=100)
    sender=models.EmailField(blank=False)
    message=models.TextField(max_length=4000)
    cc=models.BooleanField(blank=True)

    def __unicode__(self):
        return self.subject

class Member(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    occupation=models.CharField(max_length=1000,blank=True)
    company=models.CharField(max_length=1000,blank=True)
    mobile_phone=models.CharField(max_length=1000,blank=True)
    home_phone=models.CharField(max_length=1000,blank=True)
    home_fax=models.CharField(max_length=1000,blank=True)
    date_of_birth=models.DateField(blank=True)
    birth_place=models.CharField(max_length=1000,blank=True)
    if_not_alsace_Reason=models.TextField(max_length=4000,blank=True)
    venue=models.CharField(max_length=1000)
    date_membership_application=models.DateField()
    signature=models.CharField(max_length=1000)
    first_sponsor=models.CharField(max_length=1000,blank=True)
    second_sponsor=models.CharField(max_length=1000,blank=True)

    def __unicode__(self):
        return self.email

class Friend(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=1000,blank=True)
    city=models.CharField(max_length=100,blank=True)
    zip=models.CharField(max_length=100,blank=True)
    state=models.CharField(max_length=100,blank=True)

    def __unicode__(self):
        return self.email

class Album(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


from cloudinary.models import CloudinaryField
from cloudinary.utils import cloudinary_url

class Picture(models.Model):
    event = models.ForeignKey(Event, blank=True,null=True)
    album = models.ForeignKey(Album, blank=True,null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    picture = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return cloudinary_url(self.picture).build_url()

class BureauMember (models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    list_position = models.IntegerField()
    picture = CloudinaryField('image/bureau',null=True,blank=True)
    bio = models.TextField(max_length=6000,blank=True,null=True)

    def __unicode__(self):
        return self.name

class BureauMemberAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["list_position","__unicode__", "title","picture", "bio"]

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["__unicode__", "picture","event", "album", "created"]
    list_filter = ["event",'album']


class MemberAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "email"]
    list_display = ["date_membership_application","first_name","last_name","email","city","state"]

class FriendAdmin(admin.ModelAdmin):
    search_fields = ["last_name", "email"]
    list_display = ["first_name","last_name","email","city","state"]

class Contact_UsAdmin (admin.ModelAdmin):
    list_display=["sender","subject","message"]

admin.site.register(Picture, ImageAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Friend,FriendAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Contact_Us,Contact_UsAdmin)

admin.site.register(BureauMember, BureauMemberAdmin)



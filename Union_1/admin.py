from django.contrib import admin
from models import Picture,Member,Friend,Event,Contact_Us,BureauMember,FlickR_Album

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

class EventAdmin(admin.ModelAdmin):
    search_fields = ["date"]
    list_display = ["date","title","description"]

admin.site.register(Picture, ImageAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Friend,FriendAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Contact_Us,Contact_UsAdmin)

admin.site.register(FlickR_Album)

admin.site.register(BureauMember, BureauMemberAdmin)
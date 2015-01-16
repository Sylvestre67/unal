__author__ = 'Sylvestre'

from django import forms
from models import Contact_Us,Member,Friend

class ContactUs_Form(forms.ModelForm):

    sender = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'rows' : '10'}),max_length=4000)
    cc = forms.BooleanField(required=False)

    class Meta:
        model = Contact_Us

class mailchimp_form(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))


class Become_a_Member(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    city=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    zip=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    state=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    occupation=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    company=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    mobile_phone=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    home_phone=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    home_fax=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date_of_birth=forms.DateField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    birth_place=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    if_not_alsace_Reason=forms.CharField(required=False,widget=forms.Textarea(attrs={'class' : 'form-control', 'rows' : '6'}))
    venue=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date_membership_application=forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    signature=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_sponsor=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    second_sponsor=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Member

class Become_a_Friend(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    city=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    zip=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    state=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Friend

class Renewal(forms.Form):
    CHOICES=(
    ('F', 'Friend'),
    ('M', 'Member'),
    )
    member_type=forms.ChoiceField(required=False,choices=CHOICES,widget=forms.RadioSelect(attrs={'class' : 'radio_renewal'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    city=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    zip=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    state=forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))


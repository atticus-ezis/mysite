from django import forms
from django.forms import ModelForm
from .models import Author, Book, Publisher
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

class UserLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', ]


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

def clean_sender(self):
    sender = self.cleaned_data.get("sender")
    if sender.split("@")[1] != "mugna.tech":
        raise forms.ValidationError("Sender should only be from a Mugna Organization.")
    return sender


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        exclude = ('email',)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class CreateBook(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class CreatePublisher(ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"




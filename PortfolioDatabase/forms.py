from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, PortfolioItem, Hobby

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['name', 'description', 'image']

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['name', 'description', 'image']

class RegisterForm(UserCreationForm):
    pass

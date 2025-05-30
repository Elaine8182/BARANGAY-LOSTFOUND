from django import forms
from django.db import models
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'location', 'date','status','disposition', 'contact_info','image']
        exclude = ['reported_by']
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description','disposition', 'location', 'image']  # Add any other fields you use

class LostFoundItem(models.Model):
    image = models.ImageField(upload_to='images/')  # Ensure this line is present
    # Other fields...
    

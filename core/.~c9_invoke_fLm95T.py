from django import forms
from .forms import *
from registration.forms import RegistrationForm

class RegisterCreateWizardForm1(forms.Form):
    First_Name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Last_Name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Street = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    City = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    State = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Country = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Zip_Code = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Phone_Number = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Email = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Date_of_Birth = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Gender = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Shirt_Size = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Emergency_Contact_First_Name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Emergency_Contact_Last_Name = form.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Emergency_Contact_Phone_Number = form.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))

class RegisterCreateWizardForm2(forms.Form):
    cardholders_name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    credit_card_number = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_cvv = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiration_date = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))






















































































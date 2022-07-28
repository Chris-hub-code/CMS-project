from dataclasses import field
from pyexpat import model
from tkinter import Widget
from turtle import mode
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Complaint


class CreateUserForm( UserCreationForm):
    
    company = forms.CharField(max_length=60, required=True)

   

    class Meta:
        model = User
        fields=('username', 'email','password1','password2','company' )
         


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('Subject','Urgency','Type_of_complaint','Description')  
    
    
    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields['Subject'].widget.attrs['class']= 'form-control'
        self.fields['Type_of_complaint'].widget.attrs['class']= 'form-control'
        self.fields['Description'].widget.attrs['class']= 'form-control'  
        self.fields['Urgency'].widget.attrs['class']= 'form-control'  
       
        
        
        
        
        
        
        
        
        
        
        
             
        
   # widget={
          #     'Subject': forms.TextInput(attrs={'class': 'form-control'}),
           #   'Type_of)_compliant': forms.Select(attrs={'class': 'form-control'}),
         #      'Description': forms.Textarea(attrs={'class': 'form-control'}),
     #   }
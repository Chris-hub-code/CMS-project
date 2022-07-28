from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime



# Create your models here.
class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('IT-RELATED',"IT-RELATED"),('METER PROBLEM',"METER PROBLEM"),)
    URGE=(('VERY URGENT',"VERY URGENT"),('URGENT',"URGENT"),('URGENT',"URGENT"),)
    
    Subject=models.CharField(max_length=200,null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None,blank=True)
    
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200,blank=True)
    Description=models.TextField(max_length=4000,null=True,blank=True)
    Time = models.DateField(auto_now=True,blank=True)
    status=models.IntegerField(choices=STATUS,default=3)
    response=models.CharField(max_length=200,null=True,blank=True,default='None')
    Complaint_date = models.DateTimeField(auto_now_add = True,null=True)
    Feedback_date = models.DateTimeField(auto_now = True)
    Urgency=models.CharField(choices=URGE,null=True,max_length=200,blank=True)
    
    def __str__(self):
        return self.Subject
    
#class Complaint(forms.Form):
 #  STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
  #  TYPE=(('IT-RELATED',"IT-RELATED"),('METER PROBLEM',"METER PROBLEM"),)
    
  #  Subject = forms.CharField(label='Your name', max_length=100) 
   # user=models.ForeignKey(User, on_delete=models.CASCADE,default=None) 
  ## Description=models.TextField(max_length=4000,null=True) 
     
    



    
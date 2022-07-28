from django.contrib import admin
from .models import Complaint 
# Register your models here.

class CAdmin(admin.ModelAdmin):
    list_display = ('user','Subject','Type_of_complaint','Description','Time','status','response')

admin.site.register(Complaint)    
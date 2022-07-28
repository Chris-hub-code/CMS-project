from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,Complaint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm 
from django.contrib.auth.models import User


def signin(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('logggin')
        
        
    context= {'form':form}
    return render(request,'signup.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
             login(request,user)
             return redirect('dashboard')
        else:
            messages.info(request, 'incorrect credentials')
            return redirect('logggin')
            
         

         
    
    return render(request,'login.html')

@login_required(login_url='logggin')
def dashboard(request):
    return render(request,'dashboard.html')


@login_required(login_url='logggin')
def complaints(request):
     complaint_form=ComplaintForm()
     if request.method == 'POST':
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
            
            instance=complaint_form.save(commit=False)
            instance.user=request.user
            instance.save()
            messages.add_message(request,messages.SUCCESS, f'Complaint Registered!!!')
            return render(request,'dashboard.html',)
     else:
         complaint_form=ComplaintForm(request.POST)
         context={'complaint_form':complaint_form,}
         return render(request,'complaint.html',context)
    
        

def logoutpage(request):
    logout(request)
    return redirect('logggin')



def profilee(request):
    context={
        'user':request.user
    }
    
    return render(request,'profile.html', context)

def response(request):
    responses=Complaint.objects.filter(user=request.user)
    context={
        'responses':responses,
        }
    return render(request,'respone.html',context)





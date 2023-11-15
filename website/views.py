from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
# Create your views here.
def home(request):

    records = Record.objects.all()
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       # Authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            messages.success(request, "You Have Been Logged In ")
            return redirect('home')
        else:
            messages.success(request,"There was an Error LogIn In....pls try.. again..")
            return redirect('home')
    else:
        return render(request,'home.html',{'records' :records})

def navbar(request):
    return render(request,'navbar.html',{})

def login_user(request):
    pass 

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username=form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully Registered!")
            return redirect('home')
    
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})
    # return render(request, 'register.html',{})
# def home(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# SuperUser-->  admin  password --> password123

def customer_record(request,pk):
    if request.user.is_authenticated:

        customer_record= Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})
    
    else:
        messages.success(request,"You Must Be Logged In to view this page...")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_customer=Record.objects.get(id=pk)
        delete_customer.delete()
        messages.success(request,"Record deleted successfully....")
        return redirect('home')
    else:
        messages.success(request,"You Must Be Logged In to delete this record..")
        return redirect('home')
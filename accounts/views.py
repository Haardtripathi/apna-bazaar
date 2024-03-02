from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile
from products.models import *
from accounts.models import *
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError



def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'register.html')



def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/accounts/login')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    




def is_valid_gmail(email):
    validator = EmailValidator()
    try:
        validator(email)
    except ValidationError:
        return False
    







def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        user_obj = authenticate(username = email , password= password)
        print(user_obj)
        print("authenticated")
        if user_obj:
            login(request , user_obj)
            print("Logged in")
            print(user_obj.is_authenticated)

            return redirect('/')
        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'login.html')


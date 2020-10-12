from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from myapp.form import Register, Login
from django.contrib import messages
from myapp.models import register
# from django.contrib.auth.myapp.register import Registers
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import re
import random
from PIL import Image
import string
# Create your views here.


def registerform(request):
    if request.method == 'POST':

        log = Register(request.POST)
        if log.is_valid():
            empid = r''.join(random.choices(string.ascii_uppercase +
                                            string.digits, k=7))
            user = log.cleaned_data['username']

            name = log.cleaned_data['name']

            age = log.cleaned_data['age']
            email = log.cleaned_data['email']
            image = log.cleaned_data['image']
            password = log.cleaned_data['password']
            password1 = log.cleaned_data['password1']

            address = log.cleaned_data['address']

            phonenumber = log.cleaned_data['phonenumber']
            email_value = re.match(
                r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', email)
            if len(str(phonenumber)) > 12:
                messages.info(
                    request, "enter correct phone number")
                return HttpResponseRedirect('/reg/')
                if not email_value:
                    messages.info(
                        request, "enter valid email")
                return HttpResponseRedirect('/reg/')
            else:
                a = register(empid=empid, username=user, name=name, age=age, email=email, image=image,
                             password=password, address=address, phonenumber=phonenumber)
                if password == password1:
                    a.save()
                    messages.info(
                        request, 'Successfully Registered')
                    return HttpResponseRedirect('/')
                else:
                    messages.info(
                        request, 'password missmatch!')
                    return HttpResponseRedirect('/reg/')

        else:
            messages.info(
                request, 'Post request failed!')
            return HttpResponseRedirect('/reg/')
    else:
        messages.info(
            request, 'post request failed!')
        return HttpResponseRedirect('/reg/')


def loginform(request):
    c = 0
    if request.method == 'POST':

        log = Login(request.POST)
        if log.is_valid():
            allobj = register.objects.all()
            username = log.cleaned_data['username']
            password = log.cleaned_data['password']
            for i in allobj:

                if (i.username == username and i.password == password):
                    c = 1
                    currentuser = username

                # else:
                #    c=0
    if c == 1:
        request.session['currentuser'] = currentuser
        for i in allobj:
            if i.username == currentuser:
                data = i
        return render(request, 'details_1.html', {'data': data})
    else:
        messages.info(
            request, 'password and username is incorrect')
        return HttpResponseRedirect('/login/')


def view_employee_form(request):
    allobj = register.objects.all()
    return render(request, 'details.html', {'data': allobj})


def logout(request):
    return HttpResponseRedirect('/')

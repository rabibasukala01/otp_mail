import random
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import customers

from .send_mail import send_mail

# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']

        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)

            # generating new otp
            otp = str(random.random()).split(".")[1][:6]
            # extract id from db
            instance = customers.objects.filter(user=request.user)
            for d in instance:
                id = d.id
            obj = customers.objects.get(id=id)
            obj.otp = otp
            obj.save()

            send_mail(otp)
            return redirect('verify')

    return render(request, 'base.html')


def sign_up(request):
    if request.method == 'POST':

        uname = request.POST['uname']
        email = request.POST['uemail']
        password = request.POST['password']
        # creating User
        user = User.objects.create_user(uname, email, password)

        # random values for otp
        otp = str(random.random()).split(".")[1][:6]

        # extended the user model
        extended_user = customers(isverify=False, user=user, otp=otp)

        extended_user.save()
        # loging in
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            # sending otp as mail

            send_mail(otp)

        return redirect('verify')
    return render(request, 'sign_up.html')


def verify(request):
    if request.method == 'POST':
        otp_code = int(request.POST['otpcode'])
        # extracting otp from db
        instance = customers.objects.filter(user=request.user)
        for d in instance:
            otp = d.otp
            id = d.id

        if otp_code == otp:
            # updating db but selecting query with id
            obj = customers.objects.get(id=id)
            obj.isverify = True
            obj.save()
            return HttpResponse("success")
        else:
            return render(request, 'verify.html')

    return render(request, 'verify.html')

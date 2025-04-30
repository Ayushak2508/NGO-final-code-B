from django.shortcuts import render , redirect , HttpResponsePermanentRedirect
import razorpay
from django.conf import settings
from .form import *
from .models import *
import csv
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_user, logout 
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'Home.html')
# Create your views here.

def about(request):
    return render (request, 'About.html')

def work(request):
    return render (request , 'work.html')

def project(request):
    return render(request , 'Projects.html')

def media(request):
    return render(request , 'media.html')

def get(request):
    return render(request , 'get.html')

def blog(request):
    return render (request , 'blog.html')

def schooldrive(request):
    return render(request , 'schooldrive.html')

def womenhealth(request):
    return render(request , 'womenhealth.html')

def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'volin.html', {'form': form})

def volunteer_list(request):
    volunteers = VolunteerApplication.objects.all().order_by('-submitted_at')
    return render(request, 'volcard.html', {'volunteers': volunteers})



#paymanet

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.amount = donation.amount * 100  # Convert to paisa
            data = {
                "amount": donation.amount,
                "currency": "INR",
                "payment_capture": 1,
            }
            order = client.order.create(data=data)
            donation.save()

            context = {
                'donation': donation,
                'order_id': order['id'],
                'razorpay_key': settings.RAZORPAY_KEY_ID,
            }
            return render(request, 'payment_checkout.html', context)
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def download_report(request):
    # Create a response with the correct CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="women_health_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Women Reached', 'Health Camps Conducted', 'Districts Covered', 'Medical Volunteers'])  # Add relevant headers

    # Example data (replace with real data from your database)
    data = [
        ['8,500+', '35', '12', '60+'],  # Replace with actual values
    ]

    # Write data rows
    for row in data:
        writer.writerow(row)

    return response


def download_skill_report(request):
    # Create a response with the correct CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="women_skill_development_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Women Beneficiaries', 'States Covered', 'Program Timeline'])  # Headers

    # Example data (Replace with real data from your database)
    data = [
        ['1,200+', 'Rajasthan & MP', '2023 – Ongoing'],  # Example data
    ]

    # Write data rows
    for row in data:
        writer.writerow(row)

    return response

import csv
from django.http import HttpResponse

def download_health_report(request):
    # Create a response with the correct CSV headers
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="community_health_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Individuals Reached', 'States Covered', 'Program Timeline'])  # Headers

    # Example data (Replace with actual data from your database)
    data = [
        ['10,000+', 'UP, Odisha, Assam', 'Ongoing'],  # Example data
    ]

    # Write data rows
    for row in data:
        writer.writerow(row)

    return response

def empowerwomen(request):
    return render (request, 'empowerwomen.html')

def edumilestone(request):
    return render (request, 'edumilestone.html')

def healthcare(request):
    return render (request, 'healthcare.html')

def schoolinbox(request):
    return render (request, 'schoolinbox.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             messages.success(request, "Account created successfully. You can now log in.")
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})

# def login_view(request):
#     form = LoginForm(request, data=request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         login(request, form.get_user())
#         return redirect('dashboard')
#     return render(request, 'login.html', {'form': form})

# @login_required
# def dashboard_view(request):
#     return render(request, 'dashboard.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid user')
            return HttpResponsePermanentRedirect('/login/')
        user=authenticate(username=username , password=password)
        if user is None:
            messages.error(request,'Invalid password')
            return HttpResponsePermanentRedirect('/login/')
        else:
            auth_user(request,user)
            return redirect('home')
    return render(request , 'login.html')

def register_view(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        # confirm_password=request.POST.get('confirm-password')
        if User.objects.filter(username=username).exists():
            messages.info(request, 'User already Exists')
            return HttpResponsePermanentRedirect('/signup/')
        user=User.objects.create_user(first_name = firstname , last_name = lastname , email=email , username=username )
        user.set_password(password)
        user.save()
        messages.info(request,'User create sucessfully')
        return HttpResponsePermanentRedirect('/login/')
    return render(request , 'register.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


# api

from django.db import models
from django.utils.timezone import now

class Banner(models.Model):
    image_url = models.URLField(max_length=255)
    title = models.CharField(max_length=150)
    description = models.TextField()
    order = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class VisionMission(models.Model):
    vision_title = models.CharField(max_length=150)
    vision_description = models.CharField(max_length=200)
    mission_title = models.CharField(max_length=150)
    mission_description = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=now)

    def __str__(self):
        return "Vision & Mission"

class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    order = models.CharField(max_length=150)
    status = models.CharField(max_length=50, default='active')  # 'active' or 'inactive'

    def __str__(self):
        return self.label

class Initiative(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image_url = models.URLField(max_length=150)
    order = models.IntegerField(default=0)
    status = models.TextField(default='active')  # 'active' or 'inactive'

    def __str__(self):
        return self.title

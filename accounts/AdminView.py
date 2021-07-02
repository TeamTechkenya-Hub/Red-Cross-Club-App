import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import CustomUser, Admin,Member
from django.core.files.storage import FileSystemStorage
from django.urls import reverse

def admin_home(request):
    return render(request, 'admin_template/home_content.html')
import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


from accounts.models import Member, CustomUser


def student_home(request):
    member_obj=Member.objects.get(admin=request.user.id)
    return render(request,"member_template/member_home_template.html",{"member_obj":member_obj})


def add_member(request):
    return render(request,"hod_template/add_member_template.html")

def add_member_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.members.address=address
            user.save()
            messages.success(request,"Successfully Added member")
            return HttpResponseRedirect(reverse("add_member"))
        except:
            messages.error(request,"Failed to Add member")
            return HttpResponseRedirect(reverse("add_member"))
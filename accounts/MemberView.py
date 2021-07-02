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

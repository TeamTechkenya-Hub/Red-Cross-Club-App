from django.contrib import admin
from .models import Admin,Member,CustomUser

admin.site.register(Admin)
admin.site.register(Member)
admin.site.register(CustomUser)
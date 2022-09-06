from django.contrib import admin
from .models import User
# Register your models here.

# class AccountAdmin(admin.ModelAdmin):
    # list_display = [ 'name','acc_type', ]

admin.site.register(User)
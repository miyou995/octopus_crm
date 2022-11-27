from ast import In
from django.contrib import admin
from .models import Proforma, Invoice, BillItem, Bill

class BillItemInline(admin.TabularInline):
    model = BillItem
    # classes = ['collapse']


admin.site.register(Invoice)
admin.site.register(Proforma)

class BillAdmin(admin.ModelAdmin):
    list_display = ['cost']
    list_display_link = ['cost']
    inlines = [BillItemInline]

admin.site.register(Bill, BillAdmin)

from ast import In
from django.contrib import admin
from .models import Proforma, Invoice

admin.site.register(Invoice)
admin.site.register(Proforma)
# admin.site.register(BillItem)


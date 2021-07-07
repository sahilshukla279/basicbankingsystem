from django.contrib import admin
from Bankapp.models import Customer, Transaction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)
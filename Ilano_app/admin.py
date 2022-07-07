from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Seller)
admin.site.register(Order)
admin.site.register(Sell)
admin.site.register(Delivery)
admin.site.register(Review)




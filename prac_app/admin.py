from django.contrib import admin

# Register your models here.
from .models import PpAgent, PricingModel, Discounts

admin.site.register(PpAgent)
admin.site.register(PricingModel)
admin.site.register(Discounts)
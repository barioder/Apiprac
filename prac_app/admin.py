from django.contrib import admin

# Register your models here.
from .models import PpAgent, PricingModel, DiscountsModel, PhoneModel

admin.site.register(PpAgent)
admin.site.register(PricingModel)
admin.site.register(DiscountsModel)
admin.site.register(PhoneModel)
from django.contrib import admin

# Register your models here.
from .models import PpAgent, PricingModel, DiscountsModel

admin.site.register(PpAgent)
admin.site.register(PricingModel)
admin.site.register(DiscountsModel)
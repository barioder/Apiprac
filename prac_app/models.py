from django.db import models
from django.core.validators import MinValueValidator
import uuid

# Create your models here.
class PpAgent(models.Model):
    surname = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        # return self.surname_name
        return '{} {}'.format(self.surname, self.last_name)

class PricingModel(models.Model):
    name = models.CharField(max_length=30)
    base_fare = models.DecimalField(max_digits=11, decimal_places=3, validators=[MinValueValidator(0)])
    cancellation_fee = models.DecimalField(max_digits=11, decimal_places=3)
    is_active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "pricing model"

    def __str__(self) -> str:
        return f"{self.name}"

class DiscountsModel(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0)])
    vale = models.FloatField()
    class Meta:
        verbose_name_plural = "Discounts"

class PhoneModel(models.Model):
    phone_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_name = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    number_of_buttons = models.IntegerField(default=5)
    
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.phone_name} {self.phone_id}'


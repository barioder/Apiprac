from django.db import models
from django.core.validators import MinValueValidator
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

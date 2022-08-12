from django.db import models

# Create your models here.
class PpAgent(models.Model):
    surname = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        # return self.surname_name
        return '{} {}'.format(self.surname, self.last_name)


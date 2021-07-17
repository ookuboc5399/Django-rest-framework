from django.db import models

# Create your models here.

class JobOffer(models.Model):
    company_name = models.CharField(max_Length=100)



    def __str__(self):
        return self.company_name
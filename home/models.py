from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=100,unique=True)
    tagline=models.CharField(max_length=255,blank=True,null=True)
    Create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Restaurant"
        verbose_name_pural="Restaurants"
        ordering=['name']

        def __str__(self):
            return self.name
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

class About(models.Model):
    title=models.CharField(max_length=100,default="About Us")
    description=models.TextField()
    image=models.ImageField(upload_to='about_images/',blank=True,null=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="About"
        verbose_name_pural="About Sections"
    def __str__(self):
        return self.title
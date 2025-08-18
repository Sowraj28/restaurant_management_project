from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=100,unique=True)
    tagline=models.CharField(max_length=255,blank=True,null=True)
    logo=models.ImageField(upload_to='restaurant_logos/',blank=True,null=True)
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

class Contact(models.Model):
    name=models.CharField(max_length=100,blank=True)
    email=models.Emailfield()
    phone=models.CharField(max_length=20,blank=True)
    address=models.TextField(blank=True)
    message=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"{self.email} ({self.name})" if self.name else self.email

class RestaurantInfo(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"



class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=CAS)
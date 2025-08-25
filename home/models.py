from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=100,unique=True)
    tagline=models.CharField(max_length=255,blank=True,null=True)
    logo=models.ImageField(upload_to='restaurant_logos/',blank=True,null=True)
    Create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    address=models.TextField(blank=True ,null=True)

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
    address=models.TextField()
    email=models.Emailfield(blank=True,null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15 ,blank=True,null=True)

    def __str__(self):
        return self.full_name or self.user.username


class Menu(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(blank=True)
    available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='menu_images/',blank=True,null=True)
    def __str__(self):
        return f"{self.name}-Rs.{self.price}"

class Order(models.Model):
    STATUS_CHOICE=[
        ('PENDING','pending'),
        ('PROCESSING','processing'),
        ('COMPLETED','completed'),
        ('CANCELLED','cancelled')
    ]
    customer=models.Foreginkey(User,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digit=8,decimal_places=2,default=0.00)
    status=models.CharField(max_length=20,choices=STATUS_CHOICE,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order#{self.id} by{self.customer.username}-{self.status}"

class OrderItem(models.Model):
    order=models.Foreignkey(Order,on_delete=models.CASCADE,related_name="items")
    menu_item=models.Foreignkey(Menu,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f"{self.quantity}x{self.menu_item.name}"

    def get_subtotal(self):
        return self.menu_item.price*self.quantity
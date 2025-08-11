from django.contrib import admin
from .models import Restaurant
from .models import About

# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','tagline','created_at','updated_at')
    search_fields=('name','tagline')
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title','updated_at')

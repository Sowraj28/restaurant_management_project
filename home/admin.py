from django.contrib import admin
from .models import Restaurant
from .models import About
from .models import RestaurantInfo
from .models import Menu,Order
# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','tagline','created_at','updated_at')
    search_fields=('name','tagline')
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title','updated_at')

admin.site.register(RestaurantInfo)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('name','price','available')
    search_fields=('name',)
    list_filter=('available',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer_name','menu_items','quantity','created_at')
    search_fields=('customer_name',)
    list_filter=('created_at',)
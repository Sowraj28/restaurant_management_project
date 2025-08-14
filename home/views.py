from django.shortcuts import render
from .models import Restaurant 
from .models import About
from .models import Contact
from .models import RestaurantInfo
from django.db import DatabaseError

# Create your views here.
def homepage(request):
    restaurant=Restaurant.objects.first()
    context={
        'restaurant_name':restaurant.name if restaurant else 'Restaurant Name Not Set',
        'restaurant_tagline':restaurant.tagline if restaurant else '',
    }
    return render(request,'home/home.html',context)

def about(request):
    try:
        about_info=About.objects.firts()
    except DatabaseError: 
        about_info=None

    context={
        'title':about_info.title if about_info else "About Us",
        'description':about_info.description if about_info else "Description not set",
        'image_url':about_info.image_url if about_info and about_info.image else None,
    }
    return render(request,'home/about.html',context)

def contact(request):
    contact_info=Contact.objects.first()
    context={
        'title':'Contact US',
        'email': contact_info.email if contact_info else 'contact@restaurant.com',
        'phone':contact_info.phone if contact_info else '+91 8788328281',
        'address':contact_info.address if contact_info else '123 foodstreet,floavur town ,USA'
    }
    return render(request,'home/contact.html',context)

def home(request):
    restaurant=RestaurantInfo.objects.first()
    return render(request,'home/home.html',{'restaurant':restaurant})

def menu_view(request):
    menu_items=[
        {'name':'Margherita Pizza','price':8.99,'description':'Classic Cheese Pizzia with frsh basile'},
        {'name':'spaghetti carbonara','price':12.99,'description':'spicy spaghetti with cheese souce'},
        {'name':'Caser Salad','price':7.99,'description':'mixe with healty grains'},
        {'name':'Tirumisu','price':5.99,'description':'the most Wanted sweet'},
    ]
    context={
        
        'menu_items':menu_items

    }
    return render(request,'menu.html',context)
    
def reservations_view(request):
    context={
        "restaurant_name":"Flavor Town"
    }
    return render(request,"home/reservations.html",context)
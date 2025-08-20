from django.shortcuts import render, redirect
from .models import Restaurant 
from .models import About
from .models import Contact
from .models import RestaurantInfo
from django.db import DatabaseError
from .forms import FeedbackForm
from .models import Menu
# Create your views here.
def homepage(request):
    restaurant=Restaurant.objects.first()
    menu_items=Menu.objects.filter(available=True).order_by('name')[:6]
    context={
        'restaurant_name':getattr(setting,'RESTAURANT_NAME','Restaurant Name Not Set'),
        'restaurant_tagline':restaurant.tagline if restaurant else '',
        'restaurant_logo':restaurant.logo.ulr if restaurant and restaurant.logo else None,
        'menu_items':menu_items
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
    query=request.GET.get('q')
    sort_by=request.GET.get('sort','name')
    
    menu_items=Menu.objects.filter(available=True)
    if query:
        menu_items=menu_items.filter(name_icontains=query)
    if sort_by in ['name','price']:
        menu_items=menu_items.order_by(sort_by)
    context={
        'menu_items':menu_items,
        'page_title':"Our Menu",
        'query':query,
        'sort_by':sort_by,

    }
    return render(request,'menu.html',context)
    
def reservations_view(request):
    context={
        "restaurant_name":"Flavor Town"
    }
    return render(request,"home/reservations.html",context)


def feedback_view(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"home/feedback_success.html")
    else:
        form=FeedbackForm()
    return render(request,"home/feedback.html",{"form":form})


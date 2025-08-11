from django.shortcuts import render
from .models import Restaurant 
from .models import About

# Create your views here.
def homepage(request):
    restaurant=Restaurant.objects.first()
    context={
        'restaurant_name':restaurant.name if restaurant else 'Restaurant Name Not Set',
        'restaurant_tagline':restaurant.tagline if restaurant else '',
    }
    return render(request,'home/home.html',context)

def about(request):
    about_info=About.objects.firts()
    context={
        'title':about_info.title if about_info else "About Us",
        'description':about_info.description if about_info else "Description not set",
        'image_url':about_info.image_url if about_info and about_info.image else None,
    }
    return render(request,'home/about.html',context)

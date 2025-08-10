from django.shortcuts import render
from .models import Restaurant 

# Create your views here.
def homepage(request):
    restaurant=Restaurant.objects.first()
    context={
        'restaurant_name':restaurant.name if restaurant else 'Restaurant Name Not Set',
        'restaurant_tagline':restaurant.tagline if restaurant else '',
    }
    return render(request,'home/home.html',context)
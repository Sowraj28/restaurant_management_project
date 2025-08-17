from django.urls import path
from .views import homepage,about,contact,menu_view,feedback_view

urlpatterns = [
    path('',homepage,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('menu/',menu_view,name='menu'),
    path('feedback/',feedback_view,name='feedback')
]
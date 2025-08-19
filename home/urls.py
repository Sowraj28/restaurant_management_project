from django.urls import path
from .import views
app_name='restaurant'

urlpatterns = [
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu_view,name='menu'),
    path('feedback/',views.feedback_view,name='feedback')
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('pricing/',views.pricing,name='pricing'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('booking/<int:id>',views.booking,name = 'booking')
]

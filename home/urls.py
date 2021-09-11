from django.contrib import admin
from django.urls import path 
from home import views 


urlpatterns = [

     
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('home/',views.home, name='home'),
    path('interest',views.interest , name='interest'),
    path('about/',views.about , name='about'),
    path('services',views.services , name='service'),
    path('gift',views.gift , name='gift'),
    path('contact',views.contact  , name='contact'),
    path('login/',views.loginuser  , name='loginuser'), 
    path('profile/',views.profileuser  , name='profile'), 
    path('logout/',views.logoutuser  , name='logout'),
    path('changePassword/',views.changePassword  , name='changePassword'),
    path('register/',views.registeruser  , name='register'),
    path('paymentDone/',views.download , name='paymentDone'),
    path('raZorpay/',views.razorPay , name='razorpaY')
    # yaha par name/   i.e slash important hai  buit agar koi function ko call kar rahe to bikul nahi laga skte 
    
] 

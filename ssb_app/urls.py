from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    
    path('home/logout/',views.logout,name='logout'),
    path('home/appn/',views.appn,name='appn'),
    path('home/',views.home,name='home'),
]

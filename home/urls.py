from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.all_device,name="adddevice"),
    path('fb_set_val/',views.fb_set_val,name="fb_set_val"),
    
]

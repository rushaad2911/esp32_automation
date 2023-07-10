from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('btn_set_val/',views.btn_set_val,name="btn_set_val"),
    path('device/create',views.create_device,name='createdevice'),
    path('device/delete',views.delete_device,name='delete_device'),
    
    
]

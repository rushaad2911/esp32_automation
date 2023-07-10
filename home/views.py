from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Devices



import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBTb8Q82Q40HFlACuKShmwZPLTell1JE3c",
  "authDomain": "esp32-93d0c.firebaseapp.com",
  "databaseURL": "https://esp32-93d0c-default-rtdb.firebaseio.com",
  "projectId": "esp32-93d0c",
  "storageBucket": "esp32-93d0c.appspot.com",
  "messagingSenderId": "751779048414",
  "appId": "1:751779048414:web:405ecf74fbb45c70e90b4f",
  "measurementId": "G-1K67SKVEBT"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()


def home(request):
    
    d_name=request.GET.get('name')

    if d_name != "":
            database.child('test').child(d_name).set("LOW")
    else:
            print("no name")
    
    context = {"devices":Devices.objects.all()}
   
    return render(request,'home.html',context)
  


def all_device(request):
      
      device_name = database.child('test').get().val()
      context = {"device_name":device_name}
      
      return render(request,'all_device.html',context)




def fb_set_val(request):
      
      fb_val = request.GET.get('btn')
      
      fb_btn_val =  database.child('test').child(fb_val).get().val()
      
      if fb_btn_val == "HIGH":
            database.child('test').child(fb_val).set("LOW")
      else:
            database.child('test').child(fb_val).set("HIGH")

      return HttpResponseRedirect(reverse("adddevice"))



  
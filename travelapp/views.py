from django.shortcuts import render
from django.http import HttpResponse
from .models import travelapp_place

# Create your views here.

#def about(request):
   # return render(request,'about.html')
#def pasVal(request):
 #   value="nefla"
  #  return render(request,'hello.html',{'nam':value})
#def add(request):
  #  return render(request,'add.html')
#def addition(request):
  #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #res=x+y
    #return render(request,'resultAdd.html',{'result':res})
#def contact(request):
   #return HttpResponse("Contact me")
def demo(request):
    obj=tb_Place.objects.all()
    return render(request,'index.html')




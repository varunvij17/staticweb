from django.shortcuts import render
from . models import place
from . models import website

# Create your views here.
def demo(request):
    obj=place.objects.all()
    dem=website.objects.all()
    return render(request,"index1.html",{'result':obj,'myweb':dem})


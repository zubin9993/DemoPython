from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import Team
def demo(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request, "index.html",{'result':obj2,'result1':obj})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#
#     return render(request,"about.html",{'addition':res,'subs':res1,'mul': res2,'div': res3})


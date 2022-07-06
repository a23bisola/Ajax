from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
# Create your views here.


def home(request):
    return render(request, 'show.html')


def getprofiles(request):
    profiles=Profile.objects.all()
    return JsonResponse({"profiles":list(profiles.values())})

# def getprofiles(request):
#     if request.method=="POST":
#         name=request.POST["name"]
#         email=request.POST["email"]
#         bio=request.POST["bio"]
#
#         newprofile=Profile(name=name, email=email, bio=bio)
#         newprofile.save()
#         return HttpResponse("new profile added")


def createprofile(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        bio=request.POST["bio"]
        print(bio)

        newprofile=Profile(name=name, email=email, bio=bio)
        newprofile.save()
        return HttpResponse("new profile added")

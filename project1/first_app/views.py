from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("This is first_app/about page. ")
def courses(request):
    return HttpResponse("This is first_app/courses page. ")
def home(request):
    return HttpResponse("This is first app page. ")

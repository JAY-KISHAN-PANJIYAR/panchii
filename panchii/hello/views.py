from django.shortcuts import render
from django, import render
# Create your views here.
def home(request):
    return HttpResponse("Hello ")
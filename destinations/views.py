from django.shortcuts import render
from django.http import HttpResponse

def destination_list(request):
    # Your view logic here
    return HttpResponse("List of Destinations")
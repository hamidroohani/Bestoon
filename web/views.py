from json import JSONEncoder
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def submit_expense(request):
    print(request.POST)

    return JsonResponse({
        'status': 'true',
    }, encoder=JSONEncoder)

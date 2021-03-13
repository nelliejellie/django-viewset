from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testUrl(request):
    return HttpResponse('this is just a test')

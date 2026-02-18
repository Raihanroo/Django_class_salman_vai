from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def insert(req):
    return HttpResponse("cat_insert")

def update(req):
    return HttpResponse("cat_update")

def delete(req):
    return HttpResponse("cat_delete")

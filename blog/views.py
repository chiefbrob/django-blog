from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h4>Blog Home</h4>')

def about(request):
  return HttpResponse('<h4>About Blog</h4>')
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from blog.models import Blog
from django.shortcuts import render, get_object_or_404


def index(req):
    return render(req, 'pages/home.html')


def login(req):
    return render(req, 'pages/login.html')


def contact(req):
    return render(req, 'pages/contact.html')


def blogs(req):
    dataBlog = Blog.objects.all()
    return render(req, 'pages/blog.html', {'dataBlog': dataBlog})
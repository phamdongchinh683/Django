from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from blog.models import Baiviet, CategoryBlog
from django.shortcuts import render, get_object_or_404


def index(req):
    return render(req, 'template1/trangchu.html')


def login(req):
    return render(req, 'pages/login.html')


def contact(req):
    return render(req, 'pages/contact.html')


def blogs(req):
    dataBlog = Baiviet.objects.all()
    categoryBlog = CategoryBlog.objects.all()
    return render(req, 'template2/blog.html', {'dataBlog': dataBlog, 'categoryBlog': categoryBlog})

def category_blogs(req, category):
    all_categories = CategoryBlog.objects.all()
    category_data = CategoryBlog.objects.filter(categoryBlog=category)
    dataBlog = Baiviet.objects.filter(categoryBlog=category)
    return render(req, 'template3/category_blog.html', {'dataBlog': dataBlog, 'category_data': category_data, 'all_categories': all_categories})

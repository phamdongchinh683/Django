from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def layout(req):
    return render(req, 'layout/base.html')
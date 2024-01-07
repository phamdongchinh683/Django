from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    ## show default
    path('', views.index),
    path('layout/',views.layout)
]


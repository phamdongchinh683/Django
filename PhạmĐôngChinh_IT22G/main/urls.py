from django.contrib import admin
from django.urls import path, re_path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('blog/', views.blogs),
    path('contact', views.contact),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

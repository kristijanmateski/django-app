"""
URL configuration for SportProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from sportapp.views import index, add, details, delete, edit

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('add/', add, name="add"),
    path('details/<int:pk>', details, name="details"),
    path('product/delete/<int:pk>', delete, name="delete"),
    path('product/edit/<int:pk>', edit, name="edit")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

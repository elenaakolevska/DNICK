"""
URL configuration for HotelApplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tkinter.font import names

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from hotel_app.views import edit_reservation, details, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('edit_reservation/<reservation_id>', edit_reservation, name='edit_reservation'),
    path('details/<reservation_id>', details, name='details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

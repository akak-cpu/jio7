from django.contrib import admin
from django.urls import path
from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",views.index,name="index"),
    path("contact",views.contact,name="contact"),
    path("search",views.search,name="search"),
]

from django.contrib import admin
from django.urls import path,include
from App1 import views as App1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',include('App1.urls')),
    path('account/',include('users_app.urls')),
    path('',App1_views.index,name='index'),
    path('contact',App1_views.contact,name='contact'),
    path('about',App1_views.about,name='about'),
]

from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('alpacify', views.upload, name='alpacify'),
    path('share', views.share, name='share'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('credits', views.credits, name='credits'),
    path('contact', views.contact, name='contact'),
    path('privacy', views.privacy_cookies, name='privacy cookies'),
]

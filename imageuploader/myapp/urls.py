from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib import admin
urlpatterns=[
    path("",views.user_login),
    path("register/",views.register),
    path("index/",views.home),
    path('makepayment/',views.makepayment),
    path('sendemail/',views.senduseremail),
    path('logout/',views.Logout,name='logout'),
    path('contact/',views.contactform,name='contact_form'),
       
    ]

    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
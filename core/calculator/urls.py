from django.urls import path
from . import views

urlpatterns = [
    #  path('',views.peek,name='peek'),
        path('',views.about,name="about"),
        path('peek/',views.peek,name="peek"),
        path('members/', views.members, name='members'),
        path('index/', views.index, name='index'),
        path('home/', views.index, name='index'),
        path('services/', views.index, name='index'),
        path('contact/', views.index, name='index'),
        path('careers/',views.careers,name="careers")
        
]

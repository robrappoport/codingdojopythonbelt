"""beltExamProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from beltExam_app import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('login', views.login),
    path('logout', views.logout),
    path('addtrip', views.addTrip),
    path('newtrip', views.newTrip),
    path('viewtrip/<int:trip_id>', views.viewTrip),
    path('removetrip/<int:trip_id>', views.removeTrip),
    path('jointrip/<int:trip_id>', views.joinTrip)
]

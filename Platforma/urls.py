"""Platforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from backplat.views import GroupAPI, SubjectListAPI, AssignmentListAPI, AssignmentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('group/', GroupAPI.as_view()),
    path('group/<int:pk>/', GroupAPI.as_view()),
    path('group/<int:pk>/assignment/', AssignmentListAPI.as_view()),
    path('group/<int:pk>/assignment/<int:jk>/', AssignmentAPI.as_view()),
    path('my_subjects/', SubjectListAPI.as_view()),
    path('register/auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
]


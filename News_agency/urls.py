"""
URL configuration for News_agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from pydoc_data.topics import topics

from django.contrib import admin
from django.urls import path, include

from agency import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("agency.urls", namespace="agency")),
    path("topics/", views.TopicListView.as_view() , name="topic-list"),
    path("newspaper/", views.NewsPaperListView.as_view(), name="newspaper-list"),
    path("newspaper/create/", views.NewsPaperCreateView.as_view(), name="newspaper-create"),
    path("newspaper/<int:pk>/delete/", views.NewsPaperDeleteView.as_view(), name="newspaper-delete"),
    path("newspaper/<int:pk>/update/", views.NewsPaperUpdateView.as_view(), name="newspaper-update"),
    path("redactor/", views.RedactorListView.as_view(), name="redactor-list"),


]

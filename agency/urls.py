from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path("", index, name='index'),
    path("topic/", views.TopicListView.as_view(), name="topic-list"),
    path("topic/create/", views.TopicCreateView.as_view(), name="topic-create"),
    path("topic/<int:pk>/delete/", views.TopicDeleteView.as_view(), name="topic-delete"),
    path("topic/<int:pk>/update/", views.TopicUpdateView.as_view(), name="topic-update"),
    path("newspaper/", views.NewsPaperListView.as_view(), name="newspaper-list"),
    path("newspaper/create/", views.NewsPaperCreateView.as_view(), name="newspaper-create"),
    path("newspaper/<int:pk>/delete/", views.NewsPaperDeleteView.as_view(), name="newspaper-delete"),
    path("newspaper/<int:pk>/update/", views.NewsPaperUpdateView.as_view(), name="newspaper-update"),
    path("redactor/", views.RedactorListView.as_view(), name="redactor-list"),
]

app_name = "agency"

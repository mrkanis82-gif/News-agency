from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("log_out/", LogoutView.as_view(), name="logout"),
    path("", index, name='index'),
    path("topic/", views.TopicListView.as_view(), name="topic-list"),
    path("topic/create/", views.TopicCreateView.as_view(), name="topic-create"),
    path("topic/<int:pk>/delete/", views.TopicDeleteView.as_view(), name="topic-delete"),
    path("topic/<int:pk>/update/", views.TopicUpdateView.as_view(), name="topic-update"),
    path("newspaper/", views.NewsPaperListView.as_view(), name="newspaper-list"),
    path("newspaper/<int:pk>/detail/", views.NewsPaperDetailView.as_view(), name="newspaper-detail"),
    path("newspaper/create/", views.NewsPaperCreateView.as_view(), name="newspaper-create"),
    path("newspaper/<int:pk>/delete/", views.NewsPaperDeleteView.as_view(), name="newspaper-delete"),
    path("newspaper/<int:pk>/update/", views.NewsPaperUpdateView.as_view(), name="newspaper-update"),
    path("redactor/", views.RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/detail/", views.RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactor/create/", views.RedactorCreateView.as_view(), name="redactor-create"),
    path("redactor/<int:pk>/update/", views.RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactor/<int:pk>/delete/", views.RedactorDeleteView.as_view(), name="redactor-delete"),
]

app_name = "agency"

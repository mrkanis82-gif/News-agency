from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from agency.models import Topic, Redactor, NewsPaper



def index(request):
    """View function for the home page of the site."""

    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_news_paper = NewsPaper.objects.count()


    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_news_paper": num_news_paper,
    }

    return render(request, "agency/index.html", context=context)


class NewsPaperListView(LoginRequiredMixin, ListView):
    model = NewsPaper
    template_name = "agency/newspapers_list.html"
    paginate_by = 10


class RedactorListView(LoginRequiredMixin, ListView):
    model = Redactor
    template_name = "agency/redactors_list.html"
    paginate_by = 10


class TopicListView(LoginRequiredMixin, ListView):
    model = Topic
    template_name = "agency/topics_list.html"
    paginate_by = 10
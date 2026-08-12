from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.models import Topic, Redactor, NewsPaper



def index(request):
    """View function for the home page of the site."""

    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = NewsPaper.objects.count()


    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_news_paper": num_newspapers,
    }

    return render(request, "agency/index.html", context=context)


class NewsPaperListView(LoginRequiredMixin, generic.ListView):
    model = NewsPaper
    template_name = "agency/newspapers_list.html"
    paginate_by = 10


class NewsPaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = NewsPaper
    template_name = "agency/form_newspaper.html"
    success_url = reverse_lazy("agency:newspapers_list")


class NewsPaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = NewsPaper
    template_name = "agency/form_newspaper.html"
    success_url = reverse_lazy("agency:newspapers_list")


class NewsPaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPaper
    template_name = "agency/confirm_delete.html"
    success_url = reverse_lazy("agency:newspapers_list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactors_list.html"
    paginate_by = 10


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    success_url = reverse_lazy("agency:redactors_list")
    template_name = "agency/form_redactor.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    success_url = reverse_lazy("agency:redactors_list")
    template_name = "agency/form_redactor.html"


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    template_name = "agency/confirm_delete.html"
    success_url = reverse_lazy("agency:redactors_list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "agency/topics_list.html"
    paginate_by = 10


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    success_url = reverse_lazy("agency:topics_list")
    template_name = "agency/form_topic.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    template_name = "agency/form_topic.html"
    success_url = reverse_lazy("agency:topics_list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "agency/confirm_delete.html"
    success_url = reverse_lazy("agency:topics_list")

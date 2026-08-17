from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency import forms
from agency.models import Topic, Redactor, NewsPaper



def index(request):
    """View function for the home page of the site."""

    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = NewsPaper.objects.count()


    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
    }

    return render(request, "agency/index.html", context=context)


class NewsPaperListView(LoginRequiredMixin, generic.ListView):
    model = NewsPaper
    template_name = "agency/newspaper_list.html"
    paginate_by = 10


class NewsPaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = NewsPaper
    template_name = "agency/newspaper_detail.html"

class NewsPaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = NewsPaper
    fields = "__all__"
    exclude = ["date"]
    template_name = "agency/form_newspaper.html"
    success_url = reverse_lazy("agency:newspaper-list")


class NewsPaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = NewsPaper
    fields = "__all__"
    template_name = "agency/form_newspaper.html"
    success_url = reverse_lazy("agency:newspaper-list")


class NewsPaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPaper
    template_name = "agency/confirm_delete.html"
    success_url = reverse_lazy("agency:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    paginate_by = 10


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "agency/redactor_detail.html"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = forms.RedactorCreationForm
    success_url = reverse_lazy("agency:redactor-list")
    template_name = "agency/form_redactor.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = ("username", "email", "first_name", "last_name", "years_of_experience")
    success_url = reverse_lazy("agency:redactor-list")
    template_name = "agency/form_redactor.html"


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    template_name = "agency/confirm_delete.html"
    success_url = reverse_lazy("agency:redactor-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"
    paginate_by = 10


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "agency/form_topic.html"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "agency/form_topic.html"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "agency/confirm_delete.html"
    success_url = reverse_lazy("agency:topic-list")

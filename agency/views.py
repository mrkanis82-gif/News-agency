from django.shortcuts import render

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
from django.contrib.auth.models import AbstractUser
from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "topic"
        verbose_name_plural = "topics"

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"


    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class NewsPaper(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    topics = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    class Meta:
        ordering = ["title"]
        verbose_name = "newspaper"
        verbose_name_plural = "newspapers"

    def __str__(self):
        return self.title

from django.contrib.auth.models import AbstractUser
from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"


    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

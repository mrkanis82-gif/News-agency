from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from agency.models import NewsPaper, Redactor, Topic


class TopicModelTests(TestCase):
    def test_str_representation(self):
        topic = Topic.objects.create(name="Politics")

        self.assertEqual(str(topic), "Politics")


class RedactorModelTests(TestCase):
    def test_str_representation(self):
        redactor = Redactor.objects.create_user(
            username="john",
            first_name="John",
            last_name="Smith",
            password="testpassword",
        )

        self.assertEqual(str(redactor), "john (John Smith)")

    def test_get_absolute_url(self):
        redactor = Redactor.objects.create_user(
            username="john",
            password="testpassword",
        )

        self.assertEqual(
            redactor.get_absolute_url(),
            reverse("agency:redactor-detail", kwargs={"pk": redactor.pk}),
        )

    def test_years_of_experience_cannot_be_negative(self):
        redactor = Redactor(
            username="john",
            years_of_experience=-1,
        )

        with self.assertRaises(ValidationError):
            redactor.full_clean()

    def test_years_of_experience_can_be_zero(self):
        redactor = Redactor(
            username="john",
            password="testpassword",
            years_of_experience=0,
        )

        redactor.full_clean()


class NewsPaperModelTests(TestCase):
    def test_str_representation(self):
        newspaper = NewsPaper.objects.create(
            title="Daily News",
            content="News content",
        )

        self.assertEqual(str(newspaper), "Daily News")
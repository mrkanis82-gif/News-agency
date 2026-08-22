from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import NewsPaper, Redactor, Topic


class ViewTestMixin:
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
        )

        cls.topic = Topic.objects.create(
            name="Politics",
        )

        cls.redactor = Redactor.objects.create_user(
            username="redactor",
            password="testpassword",
            email="redactor@test.com",
            first_name="John",
            last_name="Smith",
            years_of_experience=5,
        )

        cls.newspaper = NewsPaper.objects.create(
            title="Test Newspaper",
            content="Test content",
        )

        cls.newspaper.topics.add(cls.topic)
        cls.newspaper.publishers.add(cls.redactor)

    def setUp(self):
        self.client.force_login(self.user)


class IndexViewTests(ViewTestMixin, TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse("agency:index"))

        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse("agency:index"))

        self.assertTemplateUsed(response, "agency/index.html")

    def test_index_view_contains_statistics(self):
        response = self.client.get(reverse("agency:index"))

        self.assertEqual(
            response.context["num_topics"],
            Topic.objects.count(),
        )
        self.assertEqual(
            response.context["num_redactors"],
            Redactor.objects.count(),
        )
        self.assertEqual(
            response.context["num_newspapers"],
            NewsPaper.objects.count(),
        )


class NewsPaperViewTests(ViewTestMixin, TestCase):
    def test_newspaper_list_view(self):
        response = self.client.get(
            reverse("agency:newspaper-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/newspaper_list.html",
        )
        self.assertIn(
            self.newspaper,
            response.context["newspaper_list"],
        )

    def test_newspaper_detail_view(self):
        response = self.client.get(
            reverse(
                "agency:newspaper-detail",
                kwargs={"pk": self.newspaper.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/newspaper_detail.html",
        )
        self.assertEqual(
            response.context["object"],
            self.newspaper,
        )

    def test_newspaper_create_view(self):
        response = self.client.get(
            reverse("agency:newspaper-create")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/form_newspaper.html",
        )

    def test_newspaper_update_view(self):
        response = self.client.get(
            reverse(
                "agency:newspaper-update",
                kwargs={"pk": self.newspaper.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/form_newspaper.html",
        )

    def test_newspaper_delete_view(self):
        response = self.client.get(
            reverse(
                "agency:newspaper-delete",
                kwargs={"pk": self.newspaper.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/confirm_delete.html",
        )


class RedactorViewTests(ViewTestMixin, TestCase):
    def test_redactor_list_view(self):
        response = self.client.get(
            reverse("agency:redactor-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/redactor_list.html",
        )
        self.assertIn(
            self.redactor,
            response.context["redactor_list"],
        )

    def test_redactor_detail_view(self):
        response = self.client.get(
            reverse(
                "agency:redactor-detail",
                kwargs={"pk": self.redactor.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/redactor_detail.html",
        )
        self.assertEqual(
            response.context["object"],
            self.redactor,
        )

    def test_redactor_create_view(self):
        response = self.client.get(
            reverse("agency:redactor-create")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/form_redactor.html",
        )

    def test_redactor_update_view(self):
        response = self.client.get(
            reverse(
                "agency:redactor-update",
                kwargs={"pk": self.redactor.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/form_redactor.html",
        )

    def test_redactor_delete_view(self):
        response = self.client.get(
            reverse(
                "agency:redactor-delete",
                kwargs={"pk": self.redactor.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/confirm_delete.html",
        )


class TopicViewTests(ViewTestMixin, TestCase):
    def test_topic_list_view(self):
        response = self.client.get(
            reverse("agency:topic-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/topic_list.html",
        )
        self.assertIn(
            self.topic,
            response.context["topic_list"],
        )

    def test_topic_create_view(self):
        response = self.client.get(
            reverse("agency:topic-create")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/form_topic.html",
        )

    def test_topic_update_view(self):
        response = self.client.get(
            reverse(
                "agency:topic-update",
                kwargs={"pk": self.topic.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/form_topic.html",
        )

    def test_topic_delete_view(self):
        response = self.client.get(
            reverse(
                "agency:topic-delete",
                kwargs={"pk": self.topic.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "agency/confirm_delete.html",
        )


class AuthenticationTests(TestCase):
    def test_newspaper_list_requires_login(self):
        response = self.client.get(
            reverse("agency:newspaper-list")
        )

        self.assertEqual(response.status_code, 302)

    def test_redactor_list_requires_login(self):
        response = self.client.get(
            reverse("agency:redactor-list")
        )

        self.assertEqual(response.status_code, 302)

    def test_topic_list_requires_login(self):
        response = self.client.get(
            reverse("agency:topic-list")
        )

        self.assertEqual(response.status_code, 302)

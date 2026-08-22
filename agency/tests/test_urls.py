from django.test import SimpleTestCase
from django.urls import reverse, resolve

from agency import views


class UrlsTests(SimpleTestCase):
    def test_index_url(self):
        url = reverse("agency:index")

        self.assertEqual(url, "/")
        self.assertEqual(resolve(url).func, views.index)

    def test_login_url(self):
        url = reverse("agency:login")

        self.assertEqual(url, "/login/")

    def test_logout_url(self):
        url = reverse("agency:logout")

        self.assertEqual(url, "/log_out/")

    def test_topic_list_url(self):
        url = reverse("agency:topic-list")

        self.assertEqual(url, "/topic/")
        self.assertEqual(resolve(url).func.view_class, views.TopicListView)

    def test_topic_create_url(self):
        url = reverse("agency:topic-create")

        self.assertEqual(url, "/topic/create/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.TopicCreateView,
        )

    def test_topic_update_url(self):
        url = reverse(
            "agency:topic-update",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/topic/1/update/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.TopicUpdateView,
        )

    def test_topic_delete_url(self):
        url = reverse(
            "agency:topic-delete",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/topic/1/delete/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.TopicDeleteView,
        )

    def test_newspaper_list_url(self):
        url = reverse("agency:newspaper-list")

        self.assertEqual(url, "/newspaper/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.NewsPaperListView,
        )

    def test_newspaper_detail_url(self):
        url = reverse(
            "agency:newspaper-detail",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/newspaper/1/detail")
        self.assertEqual(
            resolve(url).func.view_class,
            views.NewsPaperDetailView,
        )

    def test_newspaper_create_url(self):
        url = reverse("agency:newspaper-create")

        self.assertEqual(url, "/newspaper/create/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.NewsPaperCreateView,
        )

    def test_newspaper_update_url(self):
        url = reverse(
            "agency:newspaper-update",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/newspaper/1/update/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.NewsPaperUpdateView,
        )

    def test_newspaper_delete_url(self):
        url = reverse(
            "agency:newspaper-delete",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/newspaper/1/delete/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.NewsPaperDeleteView,
        )

    def test_redactor_list_url(self):
        url = reverse("agency:redactor-list")

        self.assertEqual(url, "/redactor/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.RedactorListView,
        )

    def test_redactor_detail_url(self):
        url = reverse(
            "agency:redactor-detail",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/redactor/1/detail")
        self.assertEqual(
            resolve(url).func.view_class,
            views.RedactorDetailView,
        )

    def test_redactor_create_url(self):
        url = reverse("agency:redactor-create")

        self.assertEqual(url, "/redactor/create/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.RedactorCreateView,
        )

    def test_redactor_update_url(self):
        url = reverse(
            "agency:redactor-update",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/redactor/1/update/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.RedactorUpdateView,
        )

    def test_redactor_delete_url(self):
        url = reverse(
            "agency:redactor-delete",
            kwargs={"pk": 1},
        )

        self.assertEqual(url, "/redactor/1/delete/")
        self.assertEqual(
            resolve(url).func.view_class,
            views.RedactorDeleteView,
        )
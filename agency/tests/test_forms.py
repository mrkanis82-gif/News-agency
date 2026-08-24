from django.test import TestCase

from agency.forms import NewspaperForm, RedactorCreationForm
from agency.models import NewsPaper, Redactor, Topic


class RedactorCreationFormTests(TestCase):
    def test_form_has_expected_fields(self):
        form = RedactorCreationForm()

        self.assertEqual(
            list(form.fields.keys()),
            [
                "username",
                "first_name",
                "last_name",
                "years_of_experience",
                "password1",
                "password2",
            ],
        )

    def test_form_is_valid_with_correct_data(self):
        form = RedactorCreationForm(
            data={
                "username": "john",
                "first_name": "John",
                "last_name": "Smith",
                "years_of_experience": 5,
                "password1": "StrongPassword123!",
                "password2": "StrongPassword123!",
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_is_invalid_with_negative_experience(self):
        form = RedactorCreationForm(
            data={
                "username": "john",
                "first_name": "John",
                "last_name": "Smith",
                "years_of_experience": -1,
                "password1": "StrongPassword123!",
                "password2": "StrongPassword123!",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)


class NewspaperFormTests(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create_user(
            username="john",
            password="testpassword",
        )
        self.topic = Topic.objects.create(name="Politics")

    def test_form_has_publishers_and_topics_fields(self):
        form = NewspaperForm()

        self.assertIn("publishers", form.fields)
        self.assertIn("topics", form.fields)

    def test_publishers_field_uses_checkbox_widget(self):
        form = NewspaperForm()

        self.assertEqual(
            form.fields["publishers"].widget.__class__.__name__,
            "CheckboxSelectMultiple",
        )

    def test_topics_field_uses_checkbox_widget(self):
        form = NewspaperForm()

        self.assertEqual(
            form.fields["topics"].widget.__class__.__name__,
            "CheckboxSelectMultiple",
        )

    def test_form_is_valid_with_publishers_and_topics(self):
        form = NewspaperForm(
            data={
                "title": "Daily News",
                "content": "Some news content",
                "publishers": [self.redactor.pk],
                "topics": [self.topic.pk],
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_required_fields(self):
        form = NewspaperForm(data={})

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("content", form.errors)
        self.assertIn("publishers", form.errors)
        self.assertIn("topics", form.errors)
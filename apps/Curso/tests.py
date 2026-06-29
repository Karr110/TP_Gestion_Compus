from django.test import TestCase
from django.urls import reverse

from .models import Curso


class CursoTemplateTests(TestCase):
    def test_list_view_shows_course_name(self):
        Curso.objects.create(anio="2024", division="A")

        response = self.client.get(reverse("curso:curso_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2024 A")

from django.test import TestCase
from django.urls import reverse


class NossaHistoriaViewTests(TestCase):
    def test_nossa_historia_page(self):
        response = self.client.get(reverse('nossa_historia'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nossa História')
        self.assertTemplateUsed(response, 'landing_page/nossa_historia.html')


class CursosViewTests(TestCase):
    def test_cursos_page(self):
        response = self.client.get(reverse('cursos'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fundamentos de Design UX/UI')
        self.assertEqual(len(response.context['courses']), 7)
        self.assertTemplateUsed(response, 'landing_page/cursos.html')


class NossaEquipeViewTests(TestCase):
    def test_nossa_equipe_page(self):
        response = self.client.get(reverse('nossa_equipe'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nossa equipe')
        self.assertContains(response, f'href="{reverse("pode_aprender")}"')
        self.assertTemplateUsed(response, 'landing_page/nossa_equipe.html')

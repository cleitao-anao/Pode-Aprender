from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse

from .views import MAX_LOGIN_ATTEMPTS


class PortalAlunoLoginSecurityTests(TestCase):
    VALID_EMAIL = 'aluno@podecrer.com'
    VALID_PASSWORD = '123456'

    def setUp(self):
        cache.clear()

    def _post_login(self, email='invalido@example.com', password='senhaerrada'):
        return self.client.post(reverse('portal_aluno:login'), {
            'email': email,
            'password': password,
        })

    def test_login_page_accepts_get(self):
        response = self.client.get(reverse('portal_aluno:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_rejects_other_http_methods(self):
        response = self.client.put(reverse('portal_aluno:login'))
        self.assertEqual(response.status_code, 405)

        response = self.client.delete(reverse('portal_aluno:login'))
        self.assertEqual(response.status_code, 405)

    def test_error_message_is_generic_for_wrong_password(self):
        response = self._post_login(email=self.VALID_EMAIL, password='senhaerrada')
        self.assertContains(response, 'E-mail ou senha incorretos. Tente novamente.')

    def test_error_message_is_generic_for_unknown_user(self):
        response = self._post_login(email='naoexiste@example.com', password='qualquer')
        self.assertContains(response, 'E-mail ou senha incorretos. Tente novamente.')

    def test_error_message_does_not_leak_which_field_is_wrong(self):
        wrong_password_response = self._post_login(email=self.VALID_EMAIL, password='senhaerrada')
        wrong_user_response = self._post_login(email='naoexiste@example.com', password='qualquer')

        self.assertEqual(
            self._extract_error(wrong_password_response),
            self._extract_error(wrong_user_response),
        )

    def test_account_locks_after_max_failed_attempts(self):
        for _ in range(MAX_LOGIN_ATTEMPTS):
            response = self._post_login()

        self.assertEqual(response.status_code, 429)
        self.assertContains(response, 'Muitas tentativas de login', status_code=429)

    def test_locked_ip_is_blocked_even_with_correct_credentials(self):
        for _ in range(MAX_LOGIN_ATTEMPTS):
            self._post_login()

        response = self._post_login(email=self.VALID_EMAIL, password=self.VALID_PASSWORD)

        self.assertEqual(response.status_code, 429)
        self.assertNotIn('portal_aluno_logged_in', self.client.session)

    def test_successful_login_clears_failed_attempts(self):
        for _ in range(MAX_LOGIN_ATTEMPTS - 1):
            self._post_login()

        response = self._post_login(email=self.VALID_EMAIL, password=self.VALID_PASSWORD)
        self.assertRedirects(response, reverse('portal_aluno:painel'))

        self.client.session.flush()
        response = self._post_login(email=self.VALID_EMAIL, password=self.VALID_PASSWORD)
        self.assertRedirects(response, reverse('portal_aluno:painel'))

    @staticmethod
    def _extract_error(response):
        return response.context['error_message']

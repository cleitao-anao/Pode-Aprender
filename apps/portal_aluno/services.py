import json
from datetime import timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone

from usuarios.models import Usuario

# Configuração de bloqueio simples para evitar força bruta.
MAX_LOGIN_ATTEMPTS = 5
LOGIN_WINDOW_MINUTES = 15
DUMMY_USER_EMAIL = 'aluno@podecrer.com'

# Hash seguro para a conta local de exemplo.
# Em produção, o password hasher deve ser configurado para usar bcrypt ou outro algoritmo forte.
DUMMY_USER_PASSWORD_HASH = make_password('123456')
GENERIC_LOGIN_ERROR = 'Usuário ou senha inválidos'


def sanitize_email(value: str) -> str:
    return value.strip().lower()


def sanitize_password(value: str) -> str:
    return value or ''


def validate_login_input(email: str, password: str) -> tuple[str, str]:
    email = sanitize_email(email)
    password = sanitize_password(password)

    if not email or not password:
        raise ValueError(GENERIC_LOGIN_ERROR)

    if len(password) > 128:
        raise ValueError(GENERIC_LOGIN_ERROR)

    try:
        validate_email(email)
    except ValidationError:
        raise ValueError(GENERIC_LOGIN_ERROR)

    return email, password


def get_client_ip(request) -> str:
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded:
        return forwarded.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '')


def get_rate_limit_cache_key(ip_address: str) -> str:
    return f'portal_aluno_login_attempts:{ip_address}'


def is_rate_limited(ip_address: str) -> bool:
    cache_key = get_rate_limit_cache_key(ip_address)
    record = cache.get(cache_key)

    if not record:
        return False

    if record['count'] >= MAX_LOGIN_ATTEMPTS:
        elapsed = timezone.now() - record['first_attempt']
        if elapsed < timedelta(minutes=LOGIN_WINDOW_MINUTES):
            return True
        cache.delete(cache_key)

    return False


def increment_login_attempt(ip_address: str) -> None:
    cache_key = get_rate_limit_cache_key(ip_address)
    record = cache.get(cache_key)

    if record is None:
        record = {
            'count': 1,
            'first_attempt': timezone.now(),
        }
    else:
        record['count'] += 1

    cache.set(cache_key, record, timeout=LOGIN_WINDOW_MINUTES * 60)


def authenticate_user(email: str, password: str):
    """
    Autentica o usuário a partir do banco de dados ou de uma conta de exemplo.

    Em um sistema real, aqui devem ser feitas consultas ao banco de dados via ORM ou
    consultas parametrizadas. Nunca construa SQL concatenando valores do usuário.
    """
    # Usa ORM seguro; Django sempre parametriza os valores internamente.
    user = Usuario.objects.filter(email=email, is_active=True).first()
    if user and user.check_password(password):
        return user

    # Fallback de teste local: mantém a funcionalidade atual.
    if email == DUMMY_USER_EMAIL and check_password(password, DUMMY_USER_PASSWORD_HASH):
        return True

    return None


def parse_login_payload(request):
    if request.content_type == 'application/json':
        try:
            payload = json.loads(request.body.decode('utf-8'))
            return payload.get('email', ''), payload.get('password', '')
        except json.JSONDecodeError:
            raise ValueError(GENERIC_LOGIN_ERROR)

    return request.POST.get('email', ''), request.POST.get('password', '')

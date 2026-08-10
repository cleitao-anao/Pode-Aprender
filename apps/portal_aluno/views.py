from datetime import timedelta

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache

from .services import (
    GENERIC_LOGIN_ERROR,
    authenticate_user,
    get_client_ip,
    increment_login_attempt,
    is_rate_limited,
    parse_login_payload,
    validate_login_input,
)


def get_profile(request):
    profile = request.session.get('profile')
    if not profile:
        profile = {
            'name': 'João',
            'email': 'aluno@podecrer.com',
            'course': 'Design Digital A',
            'photo_url': 'https://i.pravatar.cc/150?img=32',
            'bio': 'Novo aluno',
        }
        request.session['profile'] = profile
    return profile


def _is_json_request(request):
    content_type = request.content_type or ''
    return content_type.startswith('application/json')


@never_cache
def login(request):
    if request.session.get('portal_aluno_logged_in'):
        return redirect('portal_aluno:painel')

    error_message = ''
    is_json = _is_json_request(request)

    if request.method == 'POST':
        try:
            email, password = parse_login_payload(request)
            email, password = validate_login_input(email, password)
        except ValueError:
            if is_json:
                return JsonResponse({'success': False, 'error': GENERIC_LOGIN_ERROR}, status=401)
            error_message = GENERIC_LOGIN_ERROR
        else:
            client_ip = get_client_ip(request)
            if is_rate_limited(client_ip):
                if is_json:
                    return JsonResponse({'success': False, 'error': GENERIC_LOGIN_ERROR}, status=429)
                error_message = GENERIC_LOGIN_ERROR
            else:
                user = authenticate_user(email, password)
                if user:
                    request.session['portal_aluno_logged_in'] = True
                    request.session.set_expiry(30 * 60)
                    get_profile(request)
                    if is_json:
                        return JsonResponse({'success': True, 'redirect': reverse('portal_aluno:painel')})
                    return redirect('portal_aluno:painel')
                increment_login_attempt(client_ip)
                if is_json:
                    return JsonResponse({'success': False, 'error': GENERIC_LOGIN_ERROR}, status=401)
                error_message = GENERIC_LOGIN_ERROR

    return render(request, 'portal_aluno/login/login_aluno.html', {
        'error_message': error_message,
    })


@never_cache
def painel(request):
    if not request.session.get('portal_aluno_logged_in'):
        return redirect('portal_aluno:login')

    return render(request, 'portal_aluno/painel/painel_aluno.html', {
        'profile': get_profile(request),
        'current': 'painel',
    })


@never_cache
def grade_horario(request):
    if not request.session.get('portal_aluno_logged_in'):
        return redirect('portal_aluno:login')

    return render(request, 'portal_aluno/grade/grade_horario.html', {
        'profile': get_profile(request),
        'current': 'grade_horario',
    })


@never_cache
def perfil(request):
    if not request.session.get('portal_aluno_logged_in'):
        return redirect('portal_aluno:login')

    profile = get_profile(request)
    message = ''

    if request.method == 'POST':
        profile['name'] = request.POST.get('name', profile['name']).strip() or profile['name']
        profile['email'] = request.POST.get('email', profile['email']).strip() or profile['email']
        profile['course'] = request.POST.get('course', profile['course']).strip() or profile['course']
        profile['bio'] = request.POST.get('bio', profile['bio']).strip() or profile['bio']
        request.session['profile'] = profile
        message = 'Perfil atualizado com sucesso.'

    return render(request, 'portal_aluno/perfil/perfil_aluno.html', {
        'profile': profile,
        'message': message,
    })


def logout(request):
    request.session.flush()
    return redirect('portal_aluno:login')

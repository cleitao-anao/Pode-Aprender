from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache


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


@never_cache
def login(request):
    if request.session.get('portal_aluno_logged_in'):
        return redirect('portal_aluno:painel')

    error_message = ''

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if email == 'aluno@podecrer.com' and password == '123456':
            request.session['portal_aluno_logged_in'] = True
            get_profile(request)
            return redirect('portal_aluno:painel')

        error_message = 'E-mail ou senha incorretos. Tente novamente.'

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

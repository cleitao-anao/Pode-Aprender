from django.shortcuts import render


def login(request):
    return render(request, 'portal_aluno/login_aluno.html')
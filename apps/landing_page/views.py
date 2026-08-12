from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing_page/pode_aprender.html')


def nossa_historia(request):
    return render(request, 'landing_page/nossa_historia.html')


def cursos(request):
    courses = [
        {'title': 'Fundamentos de Design UX/UI', 'description': 'Aprenda a criar interfaces intuitivas e experiências centradas no usuário.', 'category': 'design', 'level': 'Intermediário', 'hours': 60, 'vacancies': 40, 'theme': 'purple', 'icon': 'fa-solid fa-paintbrush'},
        {'title': 'Design de Interfaces Digitais', 'description': 'Transforme ideias em produtos digitais funcionais, acessíveis e atraentes.', 'category': 'design', 'level': 'Intermediário', 'hours': 60, 'vacancies': 30, 'theme': 'purple', 'icon': 'fa-solid fa-pen-nib'},
        {'title': 'Prototipação com Figma', 'description': 'Crie protótipos navegáveis e aprenda os fundamentos de sistemas de design.', 'category': 'design', 'level': 'Iniciante', 'hours': 40, 'vacancies': 35, 'theme': 'purple', 'icon': 'fa-brands fa-figma'},
        {'title': 'Data Science com Python', 'description': 'Explore análise de dados, visualização e machine learning com Python.', 'category': 'dados', 'level': 'Intermediário', 'hours': 100, 'vacancies': 35, 'theme': 'blue', 'icon': 'fa-solid fa-terminal'},
        {'title': 'Introdução à Programação', 'description': 'Aprenda lógica, algoritmos e os primeiros passos no mundo do código.', 'category': 'programacao', 'level': 'Iniciante', 'hours': 40, 'vacancies': 25, 'theme': 'blue', 'icon': 'fa-solid fa-code'},
        {'title': 'Desenvolvimento Full Stack', 'description': 'Domine backend e frontend usando Node.js, Express, React e bancos de dados.', 'category': 'programacao', 'level': 'Avançado', 'hours': 120, 'vacancies': 25, 'theme': 'pink', 'icon': 'fa-solid fa-laptop-code'},
        {'title': 'Desenvolvimento Web Front-end', 'description': 'Construa sites responsivos e interativos com HTML, CSS e JavaScript.', 'category': 'programacao', 'level': 'Intermediário', 'hours': 100, 'vacancies': 30, 'theme': 'pink', 'icon': 'fa-solid fa-display'},
    ]
    return render(request, 'landing_page/cursos.html', {'courses': courses})


def nossa_equipe(request):
    return render(request, 'landing_page/nossa_equipe.html')

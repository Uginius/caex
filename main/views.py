from django.shortcuts import render


def index(request):
    context = {
        'title': 'First step in USA financial system'
    }
    return render(request, template_name='main/main.html', context=context)

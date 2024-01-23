from django.shortcuts import render


def index(request):
    context = {
        'title': 'Easy Crypto'
    }
    return render(request, template_name='easycrypto/easy.html', context=context)

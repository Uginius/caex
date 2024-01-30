from django.shortcuts import render

from easycrypto.models import Expertise


def index(request):
    context = {
        'title': 'Unlocking financial freedom:<br/> join the trusted path<br/> with the best partner',
        'trusted': Expertise.objects.all()
    }
    return render(request, template_name='easycrypto/easy.html', context=context)

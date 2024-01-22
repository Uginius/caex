from django.http import HttpResponse
from django.shortcuts import render

from faq.models import Ques


def faq_index(request):
    context = {
        'faqs': Ques.objects.all(),
        'title': 'Frequently asked question'
    }
    return render(request, template_name='faq/faq_index.html', context=context)

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Contact us'
    }
    return render(request, template_name='contacts/contacts.html', context=context)

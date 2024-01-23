from django.shortcuts import render, redirect

from contacts.forms import FeedbackForm
from contacts.models import Feedback


def index(request):
    context = {
        'title': 'Contact us'
    }
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bank/')
    else:
        context['form'] = FeedbackForm()
        return render(request, template_name='contacts/contacts.html', context=context)

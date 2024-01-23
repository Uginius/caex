from django.shortcuts import render, redirect

from contacts.forms import FeedbackForm
from contacts.models import Feedback, Smm


def index(request):
    context = {
        'title': 'Contact us',
        'socialmedia': Smm.objects.all()
    }
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # feedback =
            form.save()
            return redirect('contacts/contacts.html')
    else:
        context['form'] = FeedbackForm()
        return render(request, template_name='contacts/contacts.html', context=context)

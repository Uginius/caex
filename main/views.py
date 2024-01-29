from django.contrib import messages
from django.shortcuts import render, redirect

from main.forms import UserRegisterForm


def index(request):
    context = {
        'title': 'First step in USA financial system'
    }
    return render(request, template_name='main/main.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('home')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()
    context = {'title': 'Sign UP', 'form': form, }
    return render(request, 'main/register.html', context=context)

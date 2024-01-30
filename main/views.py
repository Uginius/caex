from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView

from main.forms import UserRegisterForm
from main.models import Profile


def index(request):
    context = {
        'title': 'Welcome to <span> CAEX </span>',
        'caption': 'First step in the USA financial system (тут можно еще воды налить)',
        'services': [
            {
                'title': 'Cryptocurrency exchange',
                'caption': 'Тут не хватает каких-нибудь текстов',
                'icon': 'icon-wallet.png',
            },
            {
                'title': 'Foreign currency exchange',
                'caption': '',
                'icon': 'icon-banknotes.png',

            },
            {
                'title': 'Bank account',
                'caption': 'powered&nbsp;by Neobank&nbsp;solutions.<br/>Starting Q3&nbsp;2024',
                'icon': 'icon-monitor.png',

            },
            {
                'title': 'Money transfer',
                'caption': 'starting Q3&nbsp;2024',
                'icon': 'icon-money-cloud.png',

            }
        ]
    }
    return render(request, template_name='main/main.html', context=context)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'You have successfully registered')
#             return redirect('home')
#         else:
#             messages.error(request, 'Registration error')
#     else:
#         form = UserRegisterForm()
#     context = {'title': 'Sign UP', 'form': form, }
#     return render(request, 'main/register.html', context=context)


def create_profile(user, cleaned_data):
    pf = Profile.objects.create(user=user)
    pf.crypto_exchange = cleaned_data.get('crypto_exchange')
    pf.foreign_exchange = cleaned_data.get('foreign_exchange')
    pf.bank_account = cleaned_data.get('bank_account')
    pf.money_transfer = cleaned_data.get('money_transfer')
    pf.save()


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('about-me')

    def form_valid(self, form):
        print(form.cleaned_data)
        response = super().form_valid(form)
        create_profile(user=self.object, cleaned_data=form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('home')


class AboutMeView(TemplateView):
    template_name = 'main/about-me.html'


def login_view(request: HttpRequest):
    redirect_url_authenticated = '/about-me/'
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url_authenticated)
        return render(request, 'main/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect(redirect_url_authenticated)

    return render(request, 'main/login.html', {'error': 'invalid login credentials'})

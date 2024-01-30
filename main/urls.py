from django.contrib.auth.views import LoginView
from django.urls import path
from .views import index, AboutMeView, logout_view, login_view, RegisterView

urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    # path('login/',
    #      LoginView.as_view(template_name='main/login.html', redirect_authenticated_user=True),
    #      name='login'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('logout/', logout_view, name='logout'),
]

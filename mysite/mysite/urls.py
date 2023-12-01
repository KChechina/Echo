"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', include('users.urls')),
    path("login/", views.login),
    path("register/", views.registration),
    path("authorisation/", views.authorisation),
    path("greetingscreen/", include('users.urls')),
    path("emailconfirmation/", views.emailconfirmation),
    path("onboarding1/", views.onboarding1),
    # path("profile/", views.profile),
    # path("profile_editor/", views.profile_editor),
    path("passrec1/", views.passrec1),  # восстановление пароля введение почты
    path("passrec2/", views.passrec2),  # восстановление пароля введение кода
    path("passrec3/", views.passrec3),  # новый пароль
    path("passrec4/", views.passrec4),  # пароль изменен
    path("welcomescreen/", views.welcomescreen),
    # path('user/registration/', registration),
    path('accounts/', include('django.contrib.auth.urls')),
]

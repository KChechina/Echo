from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Profile
from .forms import RegisterForm
from django.urls import reverse_lazy


# Создаем здесь представления.
def home(request):
    return render(request, "users/home.html")

@login_required
def profile_view(request):
    return render(request, "users/profile.html")

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('onboarding1')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def profile_editor(request):
    return render(request, "users/profile_editor.html")

def onboarding1_view(request):
    return render(request, "users/onboarding1.html")
# class RegisterName(FormView):
#     form_class = RegisterForm
#     template_name = 'users/greetingscreen.html'
#     success_url = reverse_lazy('welcomescreen')
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

def welcomescreen_view(request):
    return render(request, "users/welcomescreen.html")

def hobbyfeed_view(request):
    return render(request, "users/hobbyfeed.html")

def reviewsfeed_view(request):
    return render(request, "users/reviewsfeed.html")

def eventsfeed_view(request):
    return render(request, "users/eventsfeed.html")

def eventeditor_view(request):
    return render(request, "users/eventeditor.html")

def eventeditor2_view(request):
    return render(request, "users/eventeditor2.html")
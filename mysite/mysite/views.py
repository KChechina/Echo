from django.shortcuts import render



def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def profile(request):
    return render(request, 'profile.html')

def profile_editor(request):
    return render(request, 'profile_editor.html')

def authorisation(request):
    return render(request, 'authorisation.html')

# def greetingscreen(request):
#     return render(request, 'greetingscreen.html')

def emailconfirmation(request):
    return render(request, 'emailconfirmation.html')

def onboarding1(request):
    return render(request, 'onboarding1.html')

def passrec1(request):
    return render(request, 'passrec1.html')

def passrec2(request):
    return render(request, 'passrec2.html')

def passrec3(request):
    return render(request, 'passrec3.html')

def passrec4(request):
    return render(request, 'passrec4.html')

def welcomescreen(request):
    return render(request, 'welcomescreen.html')


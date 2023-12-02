from django.urls import path
from . import views
from .views import profile_view, RegisterView, profile_editor, welcomescreen_view, onboarding1_view, hobbyfeed_view, reviewsfeed_view, eventsfeed_view, eventeditor_view, eventeditor2_view



urlpatterns = [

 path('', views.home, name="home"),
 # path('users/signup/', views.registration),
 # path('greetingscreen/', views.greetingscreen, name="greetingscreen"),
 path('profile', profile_view, name="profile"),
 path('register', RegisterView.as_view(), name="register"),
 path('profile_editor', profile_editor, name="profile_editor"),
 # path('greetingscreen', RegisterName.as_view(), name="greetingscreen"),
 path('welcomescreen', welcomescreen_view, name="welcomescreen"),
 path('onboarding1', onboarding1_view, name="onboarding1"),
 path('hobbyfeed', hobbyfeed_view, name="hobbyfeed"),
 path('reviewsfeed', reviewsfeed_view, name="reviewsfeed"),
 path('eventsfeed', eventsfeed_view, name="eventsfeed"),
 path('eventeditor', eventeditor_view, name="eventeditor"),
 path('eventeditor2', eventeditor2_view, name="eventeditor2"),

]
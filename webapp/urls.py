from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
    path("",views.index, name='index'),
    path("index/",views.index, name='index'),
    path("signup/registration",views.registration, name='registration'),
    path("registration",views.registration, name='registration'),
    path("signup/",views.signup, name='signup'),
    path("index/login",views.login, name='login'),
    path("login",views.login, name='login'),
    path("home/",views.home, name='home'),
    path("home/logout",views.logout, name='logout'),
    path("home/view",views.details, name='logout'),
   
    ]
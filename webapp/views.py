from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from webapp.models import users

# Create your views here.
def index(request):
    return render(request, "index.html")
def signup(request):
    return render(request, "signup.html")
def registration(request):
    print('starting')

    if request.method == "POST":
        uname = request.POST['uname']
        email = request.POST['email']
        pswd = request.POST['pass']
        name = request.POST['name']
        if User.objects.filter(email=email).exists():
            messages.info(request,'email exist please log in')
            return redirect('/signup')
        if User.objects.filter(username=uname).exists():
            messages.info(request,'User name exist')
            return redirect('/signup')
        member = User.objects.create_user(username=uname,email=email,password=pswd,first_name=name)
        member.save()
        print('successful')
        return redirect('/')

    return render(request, "index.html")

def login(request):
    email = request.POST['email']
    pswd = request.POST['pass']
    user = auth.authenticate(username=email, password=pswd)
    if user is not None:
        auth.login(request,user)
        return redirect('/home')
    else:
        messages.info(request,'user not exist')
        return redirect('/')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def details(request):
    name = users.name
    phone = users.phone
    redirect('/home')

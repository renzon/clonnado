from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'home/pagina_login.html', {})

def base(request):
    return render(request, 'home/base.html', {})

def home(request):
    return render(request, 'home/home.html', {})

def menubar(request):
    return render(request, 'home/menubar.html', {})

def sidebar(request):
    return render(request, 'home/sidebar.html', {})
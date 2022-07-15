from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

import requests

# Create your views here.
def select_register(request):
    return render(request, 'home/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

@login_required(login_url='opcoes')
def home(request):
    return render(request, 'home/home.html', {})

def menubar(request):
    return render(request, 'home/menubar.html', {})

def sidebar(request):
    url = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=f3ddd76e328349ce8967b46f7703dfad")
    text = url.text
    data = json.loads(text)
    article = data['articles']
       
    return render(request, 'home/sidebar.html', context = {"articles" : article})

def explorar(request):
    return render(request, 'home/explorar.html', {})

def login(request):
    return render(request, 'home/login.html', {})

# def api_response(request):
#     url = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=f3ddd76e328349ce8967b46f7703dfad")
#     text = url.text
#     data = json.loads(text)
#     article = data['articles']
    
#     return render (request, context = {"articles" : article})
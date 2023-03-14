from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'MySocialNetwork/home.html')

def save_post(request):
    titulo = request.GET['Titulo']
    texto = request.GET['Texto']
    post = Post(titulo=titulo,texto=texto)
    post.save()

    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'MySocialNetwork/forum.html', context=context)
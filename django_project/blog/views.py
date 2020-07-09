from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
posts = [
    {
        'author': 'Deng Pan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '7th July 2020'
    },

    {
        'author': 'Deng Pan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '8th July 2020'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

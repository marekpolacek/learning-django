from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

def home(request):
    context = {
        'page': { 'title':'Blog home' },
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog home</h1>')

def about(request):
    return render(request, 'blog/about.html', { 'page': { 'title': 'About', 'content': 'Page content'}})
    # return HttpResponse('<h1>About this blog</h1>')
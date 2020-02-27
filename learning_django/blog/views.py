from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Marek',
        'title': 'Blog post 1',
        'content': 'First blog post content',
        'date_posted': 'Feb 26, 2020'
    },
    {
        'author': 'Marek',
        'title': 'Blog post 2',
        'content': 'Second blog post content',
        'date_posted': 'Feb 27, 2020'
    },
]

def home(request):
    context = {
        'page': { 'title':'Blog home' },
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog home</h1>')

def about(request):
    return render(request, 'blog/about.html', { 'page': { 'title': 'About', 'content': 'Page content'}})
    # return HttpResponse('<h1>About this blog</h1>')
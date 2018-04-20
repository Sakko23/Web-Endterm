from django.shortcuts import render
from .models import Blog

def bloglist(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/bloglist.html', {'blogs': blogs})


def addNew (request):
        title = request.POST['title']
        text = request.POST['text']
        blog = Blog (title=title, text=text)
        blog.save()
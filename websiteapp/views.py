from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.
def main(request):
    return render(request, 'main.html')

def write(request):
    return render(request, 'write.html')

def create(request):
    post = Blog()
    post.title = request.POST['title']
    post.pub_date = timezone.now()
    post.writer = request.POST['writer']
    post.body = request.POST['body']
    post.feelings = request.POST['feelings']
    post.image = request.FILES.get('image')
    post.save()
    return redirect('read')

def read(request):
    posts = Blog.objects
    return render(request, 'read.html', {'posts':posts})

def details(request, id):
    post = get_object_or_404(Blog, id = id)
    return render(request, 'details.html', {'post' : post})

def edit(request, id):
    edit_post = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'edit_post' : edit_post})

def update(request, id):
    update_post = Blog.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.pub_date = timezone.now()
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']
    update_post.feelings = request.POST['feelings']
    update_post.image = request.FILES.get('image')   
    update_post.save()
    return redirect('details', id)

def delete(request, id):
    delete_post = Blog.objects.get(id = id)
    delete_post.delete()
    return redirect('read')

    
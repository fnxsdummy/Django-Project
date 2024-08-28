from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Message
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import PostForm, SignUpForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



# Create your views here.

def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'delete_confirmation.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('posts')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('posts')

def chats(request):
    messages = Message.objects.all().order_by('created_at')
        
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('chats')
    else:
        form = MessageForm()
    return render(request, 'chats.html', {'messages': messages, 'form': form})
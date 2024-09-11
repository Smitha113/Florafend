# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

def blog_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comment_form': comment_form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_home')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    # Check if the request user is the author of the post
    if request.user == post.author:
        post.delete()
    return redirect('blog_home')
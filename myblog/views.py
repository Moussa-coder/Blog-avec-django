from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import CreateBlog, Comment
from .forms import BlogForm, PostForm

class PostListView(ListView):
    model = CreateBlog
    template_name = 'myblog/frontpage.html'
    context_object_name = 'posts'
    paginate_by = 3

def post_detail(request, slug):
    post = get_object_or_404(CreateBlog, slug=slug)
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = BlogForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'myblog/post_detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article créé avec succès !')
            return redirect('frontpage')
    else:
        form = PostForm()
    
    return render(request, 'myblog/post_form.html', {'form': form, 'action': 'Créer'})

def edit_post(request, slug):
    post = get_object_or_404(CreateBlog, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article modifié avec succès !')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'myblog/post_form.html', {'form': form, 'action': 'Modifier'})

def delete_post(request, slug):
    post = get_object_or_404(CreateBlog, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Article supprimé avec succès !')
        return redirect('frontpage')
    
    return render(request, 'myblog/post_confirm_delete.html', {'post': post})
     
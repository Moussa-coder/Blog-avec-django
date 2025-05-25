from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import CreateBlog, Comment
from .forms import BlogForm

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
     
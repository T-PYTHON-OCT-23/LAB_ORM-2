from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.urls import reverse

def post_list(request):
    # try:
        if "search" in request.GET:
            posts = Post.objects.filter(title__contains=request.GET["search"])
        elif "category" in request.GET:
            posts = Post.objects.filter(category=request.GET["category"])
        else:
            posts = Post.objects.all()
        
        return render(request, 'blog/post_list.html', {'posts': posts})
    # except Exception as e:
        # return render(request, 'blog/error.html')

def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    except Exception as e:
        return render(request, 'blog/error.html')

def post_create(request):
    try:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                if post.is_published:
                    post.published_at = timezone.now()
                post.save()
                return redirect(reverse('main:post_detail', kwargs={'pk': post.pk}))
        else:
            form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})
    except Exception as e:
        return render(request, 'blog/error.html')

def post_update(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            action = request.POST.get('action')

            if form.is_valid():
                post = form.save(commit=False)
                if post.is_published:
                    post.published_at = timezone.now()
                
                if action == 'edit':
                    post.save()
                    return redirect('main:post_detail', pk=post.pk)
                elif action == 'delete':
                    post.delete()
                    return redirect('main:post_list')

                post.save()
                return redirect('main:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)

        return render(request, 'blog/post_update.html', {'form': form, 'post': post})
    except Exception as e:
        return render(request, 'blog/error.html')

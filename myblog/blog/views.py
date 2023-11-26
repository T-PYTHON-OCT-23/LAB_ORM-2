# blog/views.py
from django.shortcuts import render, redirect , get_object_or_404
from .models import Post
from django.utils import timezone 
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.is_published = True
            post.published_at = timezone.now()
            post.image = request.FILES['image'] 
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


def view_post(request, post_id):
    #post = Post.objects.get(id=post_id)
    post=get_object_or_404(Post, id=post_id)
    return render(request, 'blog/view_post.html', {'post': post})
    #raise Http404("Post does not exist")
    
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            post.image = request.FILES['image']
            print(post.image) 
            return redirect('blog:view_post', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/update_post.html', {'form': form})
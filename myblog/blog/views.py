# blog/views.py
from django.shortcuts import render, redirect , get_object_or_404
from .models import Post , Comment
from django.utils import timezone 
from .forms import PostForm , CommentForm


CATEGORY_CHOICES = [
    ("tech", "Tech"),
    ("sports", "Sports"),
    ("entertainment", "Entertainment"),
    ("politics", "Politics"),
    ("fashion", "Fashion"),
    ("food", "Food"),
    ("travel", "Travel"),
    ("other", "Other"),
]

def post_list(request):
    orderby=request.GET.get('OrderBy')
    
    if orderby=="p_a":
        posts = Post.objects.all().order_by('-published_at')

    else:
        posts = Post.objects.all()

    search=request.GET.get('search')
    if search and orderby=="p_a":
        posts = Post.objects.filter(title__icontains=search).order_by('-published_at')
    
    cat = request.GET.get('category')
    
    if cat and orderby=="p_a":
        posts = Post.objects.filter(category=cat).order_by('-published_at')
        
    
    if search:
        posts = Post.objects.filter(title__icontains=search)
    
    
    if cat:
        posts = Post.objects.filter(category=cat)

    comments=Comment.objects.all().order_by('-created_at')[:5]
    
    return render(request, 'blog/post_list.html', {'posts': posts , 'categories': CATEGORY_CHOICES , 'comments' : comments})

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
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:view_post', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/view_post.html', {'post': post, 'comments': comments, 'form': form})

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
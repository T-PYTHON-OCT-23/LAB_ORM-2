from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.utils import timezone
import sqlite3

def add_blog_view(request: HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], is_publishd= True if "is_publishd" in request.POST else False, publishd_at=timezone.now() , poster=request.FILES["poster"] ,  category=request.POST["category"])
        new_post.save()

        return redirect("posts:post_home_view")

    return render(request, "blog/add.html" , {"categories" : Post.categories})



def post_home_view(request: HttpRequest):

    posts = Post.objects.all()

    return render(request, "blog/blog_home.html", {"posts" :posts})



def post_detail_view(request:HttpRequest, posts_id):
    try:
        posts = Post.objects.get(id=posts_id)
        return render(request, "blog/blog_detail.html", {"posts" : posts})
    except sqlite3.Error as er:
        print('SQLite error:404')




def update_post_view(request: HttpRequest, posts_id):

    posts = Post.objects.get(id=posts_id)

    if request.method == "POST":
        posts.title = request.POST["title"]
        posts.content = request.POST["content"]
        # posts.is_publishd = request.POST["is_publishd"]
        posts.publishd_at = request.POST["publishd_at"]
        posts.category = request.POST["category"]
        posts.poster= request.FILES["poster"]

        posts.save()

        return redirect('posts:post_detail_view', posts_id=posts.id)

    return render(request, "blog/update.html", {"posts" : posts , "categories"  : Post.categories})


def delete_post_view(request: HttpRequest, posts_id):

    posts = Post.objects.get(id=posts_id)
    posts.delete()

    return redirect("posts:post_home_view")

def search_view(request: HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        posts = Post.objects.filter(title__contains=keyword)
    else:
        posts = Post.objects.all()


    return render(request, "posts/search.html", {"posts" : posts})


def display_Blog_views(request : HttpRequest):
    if 'category' in request.GET and request.GET["category"] == 'Fashion':
        posts = Post.objects.filter(category__contains ="Fashion")

    elif 'category' in request.GET and request.GET["category"] == 'Personal_blogs':
        posts = Post.objects.filter(category__contains ="Personal blogs") 
    
    elif 'category' in request.GET and request.GET["category"] == 'Lifestyle':
        posts = Post.objects.filter(category__contains ="Lifestyle")
    
    elif 'category' in request.GET and request.GET["category"] == 'News_blogs':
        posts = Post.objects.filter(category__contains ="News blogs")

    elif 'category' in request.GET and request.GET["category"] == 'technology':
        posts = Post.objects.filter(category__contains ="technologys")

    else:
        posts = Post.objects.all()
    return render(request , 'posts/blog_home.html' , {"posts" : posts})
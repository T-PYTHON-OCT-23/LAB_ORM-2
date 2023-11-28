from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog, Review

# Create your views here.


def home(request: HttpRequest):
    return render(request, "main/home.html")


def add_blog(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(
            name=request.POST["name"], paragraph=request.POST["paragraph"], release_date=request.POST["release_date"], category=request.POST["category"], image=request.FILES["image"])
        new_blog.save()

        return redirect("main:read_blog")

    return render(request, "main/add.html", {"categories": Blog.categories})


def read_blog(request: HttpRequest):

    blog = Blog.objects.all()

    return render(request, "main/read.html", {"blog": blog})


def detail_blog(request: HttpRequest, blog_id):
    blog_detail = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        new_blog = Review(
            Blog=blog_detail, full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])
        new_blog.save()

    review = Review.objects.filter(Blog=blog_detail)
    return render(request, "main/detail.html", {"blog": blog_detail, "review": review})


def update_blog(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        Blog.name = request.POST["name"]
        Blog.paragraph = request.POST["paragraph"]
        Blog.release_date = request.POST["release_date"]
        Blog.category = request.POST["category"]
        Blog.image = request.FILES["image"]
        Blog.save()

        return redirect("main:read_blog", blog_id=blog.id)
    return render(request, "main/update.html", {"blog": blog},  {"categories": Blog.categories})


def delete_blog(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    Blog.delete()
    return redirect(request, "main:read_blog", {"blog": blog})


def search(request: HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        blog = Blog.objects.filter(name__contains=keyword)
    else:
        blog = Blog.objects.all()

    return render(request, "main/search.html", {"blog": blog})

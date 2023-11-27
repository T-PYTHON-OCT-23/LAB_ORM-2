from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from .models import Blog
from django.utils import timezone

# Create your views here.


def add_post_view(request: HttpRequest):

    if request.method == "POST":
        read_blog_item = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"],published_at=request.POST["published_at"] ,category=request.POST["category"], image=request.FILES["image"])
        read_blog_item.save()

        return redirect("blogApp:read_blog_view")

    return render(request, "blogApp/add_post.html" , {"categories" : Blog.categories} )




def read_blog_view(request: HttpRequest):

    blogs = Blog.objects.all()

    if 'search' in request.GET:
        keyword = request.GET["search"]
        blogs = Blog.objects.filter(title__icontains= keyword)
    else:
        blogs = Blog.objects.all()

    # blogs = Blog.objects.all().order_by("published_at")



    return render(request, "blogApp/read_blog.html", {"blogs" : blogs})

# handle with not found pages 
try:
    def detail_blog_view(request:HttpRequest , blog_id):

        blog = Blog.objects.get(id=blog_id)

        return render(request , "blogApp/detail.html" , {"blog":blog})
except Exception as e:
    print(e)

try:
    def update_view(request :HttpRequest , blog_id):
        blog=Blog.objects.get(id=blog_id)
        if request.method == "POST":
            blog.title = request.POST["title"]
            blog.content = request.POST["content"]
            blog.is_published = request.POST["is_published"]
            blog.published_at = request.POST["published_at"]
            blog.category = request.POST["category" , " "]
            blog.image = request.FILES["image" , blog.image]
            blog.save()

            return redirect("blogApp:read_blog_view" )
        return render(request ,"blogApp/update.html" ,  {"blog":blog , "categories"  : Blog.categories})
except Exception as e:
    print(e)


try:
    def delete_view(request :HttpRequest , blog_id):
        blog=Blog.objects.get(id = blog_id)
        blog.delete()
        return redirect("blogApp:read_blog_view")
except Exception as e:
    print(e)




def category_view (request :HttpRequest , item):


    if item== "Health":
        blogs = Blog.objects.filter(category= "Health")
    elif item == "Stories":
        blogs = Blog.objects.filter(category= "Stories")
    elif item == "Science":
        blogs = Blog.objects.filter(category= "Science")
    else:
        blogs = Blog.objects.all()

    return render(request, "blogApp/read_blog.html", {"blogs" : blogs})



from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from django.utils import timezone
# Create your views here.



def add_blog_views(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],content=request.POST["content"],is_published=request.POST["is_published"],category=request.POST["category"],published_at=timezone.now())
        if "image" in request.FILES:
            new_blog.image=request.FILES["image"]
        new_blog.save()
        return redirect("blog:home_blog_views")

    return render(request, "blog/add_blog.html",{"categories":Blog.categories})



def home_blog_views(request: HttpRequest):
    if "category" in request.GET :
        blog =Blog.objects.filter(category=request.GET["category"])
    else:
        blog =Blog.objects.all()

    return render(request, "blog/home_blog.html", {"blogs":blog})

def details_blog_views(request: HttpRequest,blog_id):
        try:
            blogs=Blog.objects.get(id=blog_id)
           
        except:
            return render(request, "blog/page_not_found.html")
         
        return render(request,"blog/details_blog.html",{"blogs":blogs})
             
def updated_blog(request:HttpRequest, blog_id):
    blogs= Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blogs.title = request.POST["title"]
        blogs.content = request.POST["content"]
        blogs.is_published = request.POST["is_published"]
        blogs.published_at=timezone.now()
        blogs.category=request.POST["category"]
        blogs.save()

        return redirect('blog:details_blog_views', blog_id=blogs.id)
     
    return render(request,"blog/updated_blog.html",{"blogs":blogs ,"categories":Blog.categories})

def delete_blog_views (request:HttpRequest, blog_id):
    blogs= Blog.objects.get(id=blog_id)
    blogs.delete()

    return redirect( "blog:home_blog_views")

def search_blog_views(request:HttpRequest):
    if "search" in request.GET:
        return_search=request.GET["search"]
        blog=Blog.objects.filter(title__contains=return_search)
    else:
        blog = Blog.objects.all()

    return render(request, "blog/search.html",{"blogs":blog})

# def home_views_category(request:HttpRequest,item):
    
#     blog= Blog.objects.filter(category=item)
    
#     return render(request, "blog/home_blog.html", {"blogs":blog})
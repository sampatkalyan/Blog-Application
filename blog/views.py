from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import blog, Category,Tags
from .forms import blogform
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db import IntegrityError
# Create your views here.

def blogdetails(request, blog_slug):
    single_blog=blog.objects.get(slug= blog_slug)
    context={
        'single_blog':single_blog,
        'user':request.user,
     }
    return render(request, 'blogs/blog.html', context)

def search(request):
    blogs=blog.objects.all()
    categories=Category.objects.all()
    if 'blogname' in request.GET:
        title=request.GET['blogname']
        if title:
            blogs=blog.objects.filter(title__icontains=title)
    context={
        'blogs':blogs,
        'categories':categories
    }
    return render(request, 'home.html', context)

def filter(request):
    categories=Category.objects.all()
    if 'category' in request.GET:
        category=request.GET.getlist('category')
        if category:
            print(category)
            blogs=blog.objects.filter(category__category__in=category)
                
    context={
        'blogs':blogs,
        'categories':categories
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        user_blogs=blog.objects.filter(author=request.user)
        context={
            'user_blogs':user_blogs
        }
        return render(request, 'blogs/dashboard.html', context)

@login_required(login_url='login')
def createblog(request):
    newblog=blogform()
    if request.method == 'POST':
        newblog=blogform(request.POST, request.FILES)
        if newblog.is_valid():
            try:
                title=newblog.cleaned_data['title']
                image=newblog.cleaned_data['image']
                body=newblog.cleaned_data['body']
                tags=newblog.cleaned_data['tags']
                category=newblog.cleaned_data['category']
                author=request.user
                createdblog=blog.objects.create(title=title, slug=slugify([title, author.pk]), image=image, body=body, category=category, author=author)
                createdblog.save()
                for tag in tags:
                    createdblog.tags.add(tag)
            
                return redirect('dashboard')
            except IntegrityError:
                message='Title cannot be same'
                context={
                    'form': newblog,
                    'message': message
                        }
                return render(request, 'blogs/createblog.html', context) 
    context={
        'form': newblog
    }
    return render(request, 'blogs/createblog.html', context)

@login_required(login_url='login')
def updateblog(request, id):
    tobeupdateblog=blog.objects.get(id=id)
    print(tobeupdateblog)
    newblog=blogform(request.POST or None, request.FILES or None,  instance=tobeupdateblog)
    if newblog.is_valid():
        newblog.save()
        return redirect('dashboard')
    else:
        context={
            'form': newblog,
            'blog':tobeupdateblog
        }
        return render(request, 'blogs/updateblog.html', context)

@login_required(login_url='login')
def deleteblog(request):
    if request.method == 'GET':
        bloglist=request.GET.getlist('blogs')
        print(bloglist)
        userblogs=blog.objects.filter(pk__in=bloglist, author=request.user)
        print(userblogs)
        userblogs.delete()
        return redirect('dashboard')
    return redirect('dashboard')
    

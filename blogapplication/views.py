from django.shortcuts import render
from blog.models import blog, Category

def bloglist(request):
    blogs= blog.objects.all()
    categories=Category.objects.all()
    context={
        'blogs':blogs,
        'categories':categories
    }
    return render(request, 'home.html', context)
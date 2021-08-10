from django.urls import path
from . import views

urlpatterns = [
    path('blog/<slug:blog_slug>/', view=views.blogdetails, name="blogdetails"),
    path('search/', view=views.search, name="search"),
    path('filter/', view=views.filter, name="filter"),
    path('dashboard/', view=views.dashboard, name='dashboard'),
    path('dashboard/create/', view=views.createblog, name='createblog'),
    path('dashboard/update/<id>/', view=views.updateblog, name='updateblog'),
    path('dashboard/delete/', view=views.deleteblog, name="deleteblog")
]

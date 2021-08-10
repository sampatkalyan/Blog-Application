from django.urls import path
from . import views

urlpatterns = [
    path('registration/', view=views.createuser, name='createuser'),
    path('login/', view=views.login, name='login'),
    path('logout/', view=views.logout, name='logout')
]

from django.shortcuts import redirect, render
from .forms import Registrationform
from .models import CustomUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def createuser(request):
    if request.method == 'POST':
        form=Registrationform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= CustomUser.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    else:
        form = Registrationform()
    context={
        'form':form
    }
    
    return render(request, 'users/registration.html', context)

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user= auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blogs')
        else:
            invalid= "Invalid credentials"
            context={
                'invalid': invalid
            }
            return render(request, 'users/login.html', context )
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logout(request):
    user=request.user
    auth.logout(request)
    return redirect('blogs')
        
    

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField 
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email Field is required")
        if not username:
            raise ValueError("Username is required")
        user=self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user= self.create_user(email=self.normalize_email(email), username=username,password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email=models.EmailField(verbose_name='Email', unique=True)
    username=models.CharField(unique=True, max_length=50)
    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects=MyUserManager()

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, add_label):
        return True

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display=('email','username', 'password','is_active')
    readonly_fields=['password',]
    ordering=['date_joined']
    list_display_links=('email', 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(CustomUser,CustomUserAdmin)
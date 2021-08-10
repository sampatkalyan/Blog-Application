from django.contrib import admin
from .models import blog, Tags, Category

# Register your models here.
class blogAdmin(admin.ModelAdmin):
    list_display=('title',"author",)
    prepopulated_fields={'slug':('title','author')}
admin.site.register(blog, blogAdmin)
admin.site.register(Tags)
admin.site.register(Category)

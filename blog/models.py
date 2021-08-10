from django.db import models
from users.models import CustomUser
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(unique=True)
    image=models.ImageField(upload_to="blogs/blog", max_length=250)
    category=models.ForeignKey("Category", verbose_name="Category", on_delete=models.CASCADE)
    tags=models.ManyToManyField("Tags", blank=True)
    body=models.TextField()
    author=models.ForeignKey(CustomUser, verbose_name="Author", on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.title

        

class Tags(models.Model):
    tags=models.CharField(max_length=50)

    class Meta:
        verbose_name='Tag'
        verbose_name_plural='Tags'

    def __str__(self):
        return self.tags

class Category(models.Model):
    category=models.CharField(max_length=250)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'


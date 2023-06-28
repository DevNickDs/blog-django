from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=100, null=None, blank=None)
    state = models.BooleanField('Category Activated/Category Deactivated', default=True)
    created_at = models.DateTimeField('Creation Date', auto_now_add=True)
    updated_at = models.DateTimeField('Update Date', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('Author name', max_length=150, null=None, blank=None)
    last_name = models.CharField('Author last name', max_length=150, null=None, blank=None)
    email = models.EmailField('Email address', null=None, blank=None)
    facebook = models.URLField('Facebook' , null=True, blank=True)
    twitter = models.URLField('Twitter' , null=True, blank=True)
    instagram = models.URLField('Instagram' , null=True, blank=True)
    state = models.BooleanField('Active Author/Non-active Author', default=True)
    created_at = models.DateTimeField('Creation Date', auto_now_add=True)
    updated_at = models.DateTimeField('Update Date', auto_now=True)

    class Meta:
        verbose_name = ('Author')
        verbose_name_plural = ('Authors')

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Post(models.Model):
    title = models.CharField('Title', max_length=80, null=None, blank=None)
    slug = models.CharField('Slug', max_length=100, null=None, blank=None)
    description = models.CharField('Description', max_length=150, null=None, blank=None)
    content = RichTextField('Content')
    image = models.URLField(max_length=255, null=None, blank=None)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.BooleanField('Published/Not Published', default=True)
    created_at = models.DateTimeField('Creation Date', auto_now_add=True)
    updated_at = models.DateTimeField('Update Date', auto_now=True)

    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')

    def __str__(self):
        return self.title

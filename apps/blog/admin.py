from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'state', 'created_at', 'updated_at')

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'last_name', 'email']
    list_display = ('name', 'last_name', 'email', 'state', 'created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
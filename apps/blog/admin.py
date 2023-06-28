from django.contrib import admin
from .models import Category, Author
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'state', 'created_at', 'updated_at')
    resource_classes = [CategoryResource]

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'last_name', 'email']
    list_display = ('name', 'last_name', 'email', 'state', 'created_at', 'updated_at')
    resource_classes = [AuthorResource]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
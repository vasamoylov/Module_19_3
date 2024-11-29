from django.contrib import admin
from .models import Author, Post


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date')
    list_filter = ('title', 'create_date')
    search_fields = ('title', 'create_date')
    
from django.contrib import admin
from .models import Author, Category, Post, Comment, Tag

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)

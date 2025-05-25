from django.contrib import admin
from .models import CreateBlog, Comment

@admin.register(CreateBlog)
class CreateBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('title', 'intro', 'body')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('name', 'email', 'body')

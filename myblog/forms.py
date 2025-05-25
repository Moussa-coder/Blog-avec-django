from django import forms
from .models import Comment, CreateBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = CreateBlog
        fields = ['title', 'slug', 'intro', 'body', 'image', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'accept': 'video/mp4,video/webm,video/ogg'}),
        }
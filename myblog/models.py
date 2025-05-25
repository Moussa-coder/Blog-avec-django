from django.db import models

# Create your models here.
class CreateBlog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200) # pour les urls
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='media', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True, help_text="Formats acceptés : MP4, WebM, Ogg")
    date_added = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['-date_added'] # les plus recents en premier

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(CreateBlog, related_name='comments', on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length=100, default='inconnu')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return f'{self.name} a commenté {self.post.title}'


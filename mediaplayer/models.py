from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class UploadMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="upload_user")
    title = models.CharField(max_length=1000, unique=False)
    thumbnail = models.ImageField(upload_to="thumbnail", null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=1300)
    movie = models.FileField(upload_to="movies", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=1000, null=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def get_absolute_url(self):
        return reverse("read-more", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    upload_movie = models.ForeignKey(UploadMovie, on_delete=models.CASCADE, related_name="comments")
    full_name = models.CharField(max_length=250)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.upload_movie.title







    
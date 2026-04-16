from django.db import models

class Question(models.Model):
    title = models.TextField()
    description = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models. TextField()
    published_date =  models.DateField(blank=True, null=True, auto_now=True)
    author = models.ManyToManyField(Author, related_name="posts")
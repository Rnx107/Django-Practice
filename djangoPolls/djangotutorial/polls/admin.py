from django.contrib import admin
from .models import Question, Author, Post

# Register your models here.
admin.site.register(Question)
admin.site.register(Author)
admin.site.register(Post)
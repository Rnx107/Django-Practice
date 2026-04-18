from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Author, Post

def index(request):
    #fetch all question records
    questions = Question.objects.all()

    #context passing
    context = {
        # content from database
        'questions': questions,
        # static context
        'title': 'Hello World'
    }
    return render(request, 'polls/quiz.html', context)

def test(request):
    authors = Author.objects.all()
    # posts = Post.objects.all()
    # This fetches all posts and their authors in just two queries
    # Solves n+1 problem
    posts = Post.objects.prefetch_related('author').all()
    context = {
        'authors': authors,
        'posts':posts
    }
    return render(request, 'polls/post.html', context)

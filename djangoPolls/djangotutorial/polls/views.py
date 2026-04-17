from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    #fetch all question records
    questions = Question.objects.all()

    #context passing
    context = {
        'questions': questions
    }
    return render(request, 'polls/base.html', context)

def test(request):
    return HttpResponse("Test")

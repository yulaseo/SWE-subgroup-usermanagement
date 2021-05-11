from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the feedback index.")

def give_feedback(request):
    return render(request, 'feedback/give_feedback.html')

def reply_feedback(request):
    return render(request, 'feedback/reply_feedback.html')
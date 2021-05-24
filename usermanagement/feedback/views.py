from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the feedback index.")

def feedback_list(request):
    return render(request, 'feedback/feedback_list.html')

def feedback_detail(request):
    return render(request, 'feedback/feedback_detail.html')
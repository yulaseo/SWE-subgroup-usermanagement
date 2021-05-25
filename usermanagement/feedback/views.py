from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback


def feedback_list(request):
    feedbacks = Feedback.objects.all()
    context = {
            'feedbacks': feedbacks
        }

    return render(request, 'feedback/feedback_list.html', context)


def feedback_detail(request, id):
    feedback = Feedback.objects.get(id = id)
    context = {
        'feedback': feedback
    }

    return render(request, 'feedback/feedback_detail.html', context)


def add_feedback(request):
    return render(request, 'feedback/add_feedback.html')


def add_feedback_action(request):
    pass
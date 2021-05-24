from django.shortcuts import render
from django.http import HttpResponse


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
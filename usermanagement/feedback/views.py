from django.shortcuts import render, redirect
from django.http import HttpResponse
from .IdGen import IdGen
from .feedbackDAO import FeedbackDAO
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from .models import Feedback


def feedback_list(request):
    feedbacks = FeedbackDAO.getFeedbacks()
    context = {
            'feedbacks': feedbacks
        }

    return render(request, 'feedback/feedback_list.html', context)


def feedback_detail(request, id):
    feedback = FeedbackDAO.getFeedback(id)
    context = {
        'feedback': feedback
    }

    return render(request, 'feedback/feedback_detail.html', context)
    

def add_feedback(request):
    return render(request, 'feedback/add_feedback.html')
    

def id_generate(request):
    new_id = IdGen.generateID()
    return HttpResponse(new_id)


def get_user_id(request):
    return "USERID"


def add_feedback_action(request):
    if request.method != "POST":
        return redirect('add_feedback')
    FeedbackDAO.save_feedback(request.POST['anonymity'], get_user_id(request), request.POST['title'], request.POST['content'], IdGen.generateID())
    messages.info(request, "The new feedback has been successfully sent.")
    return HttpResponseRedirect('add-feedback')
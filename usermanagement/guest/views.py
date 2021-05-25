from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Guest, Book
from .IdGen import IdGen
from .NewComerChecker import NewComerChecker


def logout(request):
    auth.logout(request)
    return redirect('login')


def search_guest(request):
    guests = Guest.objects.all()

    searchParam = request.POST.get('searchParam', '')
    if searchParam:
        guestList = guests.filter(Q(name__icontains=searchParam) | Q(userid__icontains=searchParam))
        context = {
            'guests': guestList,
            'searchParam': searchParam
        }
        return render(request, 'guest/search_guest.html', context)

    return render(request, 'guest/search_guest.html')


def guest_detail(request, userid):
    guest = Guest.objects.get(userid = userid)
    context = {
        'name': guest.name,
        'id': guest.userid
    }
    return render(request, 'guest/guest_detail.html', context)


def add_guest(request):
    return render(request, 'guest/add_guest.html')


def add_guest_action(request):
    if request.method != "POST" or not NewComerChecker.check(request.POST):
        return redirect('add_guest')
    

def id_generate(request):
    new_id = IdGen.generateID()
    return HttpResponse(new_id)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Guest, Book
from django.db.models import Q


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
    pass
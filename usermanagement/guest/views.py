from django.shortcuts import render
from django.http import HttpResponse
from .forms import RestrictForm


def index(request):
    return HttpResponse("Hello")


def logout(request):
    auth.logout(request)
    return redirect('login')


def search_guest(request):
    guests = Guest.objects.all()

    searchParam = request.POST.get('searchParam', '')
    if searchParam:
        guestList = guests.filter(Q(name__icontains=searchParam) | Q(userid__icontains=searchParam))
        context = {
            'guests': guestList
        }
        return render(request, 'guest/search_guest.html', context)

    return render(request, 'guest/search_guest.html')


def guest_detail(request, userid):
    guest = Guest.objects.get(userid = userid)
    context = {
        'guest': guest
    }

    return render(request, 'guest/guest_detail.html', context)
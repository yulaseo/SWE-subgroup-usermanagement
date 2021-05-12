from django.shortcuts import render
from django.http import HttpResponse
from .forms import RestrictForm

def index(request):
    return HttpResponse("Hello")

def delete_or_restrict(request):
    # 맨 처음 들어오면 검색창 보여줌
    # 검색한 결과(게스트 리스트) 보여줌, 옆에 delete, restrict 버튼 있음
    # delete 누르면 게스트 삭제됨, 게스트 반납하지 않은 책 있으면 메시지 띄움
    # restrict 누르면 period 결정하는 창으로 넘어감. 그 창에서 날짜 입력하고 submit 누르면 제한됨

    guests = Guest.objects.all()

    searchParam = request.POST.get('searchParam', '')
    if searchParam:
        guestList = guests.filter(Q(name__icontains=searchParam) | Q(userid__icontains=searchParam))
        context = {
            'guests': guestList
        }
        return render(request, 'guest/delete_restrict.html', context)

    return render(request, 'guest/delete_restrict.html')


def delete(request, guest_name):
    guest = Guest.objects.get(name=guest_name)
    guest.delete()
    return redirect('delete_restrict')


def restrict(request, guest_name):
    # set period page
    guest = Guest.objects.get(name=guest_name)
    if request.method == 'POST':
        form = RestrictForm(request.POST)
        if form.is_valid:
            guest = form.save(commit=False)
            guest.name = name
            guest.restricted_status = True
            guest.save()
            return redirect('delete_restrict')
    else:
        form = RestrictForm()
    return render(request, 'guest/set_period.html', {'form': form})

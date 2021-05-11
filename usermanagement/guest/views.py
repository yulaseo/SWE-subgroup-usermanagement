from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def delete_or_restrict(request):
    # 맨 처음 들어오면 검색창 보여줌
    # 검색한 결과(게스트 리스트) 보여줌, 옆에 delete, restrict 버튼 있음
    # delete 누르면 게스트 삭제됨, 게스트 반납하지 않은 책 있으면 메시지 띄움
    # restrict 누르면 period 결정하는 창으로 넘어감. 그 창에서 날짜 입력하고 submit 누르면 제한됨
    return render(request, 'guest/delete_restrict.html')


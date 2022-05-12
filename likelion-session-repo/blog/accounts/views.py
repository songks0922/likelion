from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(request, username=username, password=password)
        # 해당 user 객체가 존재한다면(객체가 존재하지 않는다면 none을 반환할 텐데, none이 not이니까 존재한다면!)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':  # 값이 넘겨졌을 경우
        if request.POST['password1'] == request.POST['password2']:  # password 1,2입력된 값이 같다면
            # user 객체를 새로 생성
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            user.save()
            return render(request,'main.html')  # 첫화면으로
    return render(request, 'signup.html')


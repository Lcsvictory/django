from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from common.forms import UserForm

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST": # 정상적인 회원가입 post요청일떄.
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # 저장된 user 객체를 반환받음
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:  # 인증 성공
                login(request, user)
                return redirect('index')
    else:
        form = UserForm() # get요청일때 or 회원가입 데이터가 비정상일때.
    return render(request, 'common/signup.html', {'form':form})
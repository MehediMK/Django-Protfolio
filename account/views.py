from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def user_log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')

            # print('username: ' +username)
        else:
            print('user not found.')
    return render(request,'./auth/login.html',{})

def user_logout(request):
    logout(request)
    return redirect('login')
    

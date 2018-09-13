from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.

def acc_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("/crm/")
        else:
            print("用户或密码不正确")
            return render(request, "login.html")

    return render(request,"login.html")

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
	if request.user.is_authenticated: #jaba user register huncha
		return render(request,'main/users.html',{'message':None})

def login_view(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(request, username = username, password = password)
	if user is not None:
		login(request, user)
		return redirect("users:index")
	else:
		return render(request,'main/login.html',
			{"message":"Invalid credential"})


def logout_view(request):
	logout(request)
	return render(request,'main/login.html',{'message':'Logged out'})
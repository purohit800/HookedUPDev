from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from datetime import datetime
from Hookups.models import Join

def home(request):
	return render(request,'Hookup/home.html')

def signupuser(request):
	if request.method=='GET':
		return render(request,'Hookup/signupuser.html',{'form':UserCreationForm()})
	else:
		if request.POST['password1']==request.POST['password2']:
			try:
				user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
				user.save()
				login(request,user)
				return redirect('home')

			except IntegrityError:
				return render(request,'Hookup/signupuser.html',{'form':UserCreationForm(),'error':'UserName Already Taken'})

		else:
			return render(request,'Hookup/signupuser.html',{'form':UserCreationForm(),'error':'Password and Confirm Password is not same'})

def loginuser(request):
	if request.method=='GET':
		return render(request,'Hookup/loginuser.html',{'form':AuthenticationForm()})
	else:
		user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
		if user is None:
			return render(request,'Hookup/loginuser.html',{'form':AuthenticationForm(),'error':'Invalid UserName Or Password'})
		else:
			login(request,user)
			return redirect('home')

		

def logoutuser(request):
	if request.method=='POST':
		logout(request)
		return redirect('home')

def join(request):
	if request.method == "POST":
		name = request.POST.get('name')
		title = request.POST.get('title')
		desc = request.POST.get('desc')
		email = request.POST.get('email')
		join = Join(name=name, title=title, desc=desc, email=email, date=datetime.today())
		join.save()
	return render(request, 'join.html')
	return redirect('home')

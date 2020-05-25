from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from UserApp.models import UserProfileInfo
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from itertools import *

# Create your views here.
def index(request):
	return render(request,'UserApp/home.html')

@login_required
def special_1(request):
	return HttpResponse("you're logged in!")

@login_required
def profile(request):
	obj = request.user.username
	#print(obj)
	userPro = UserProfileInfo.objects.filter(user__username=obj)
	args = {'user': request.user,'dob':userPro.values('DOB'),}
	return render(request,'UserApp/profile.html',args)

@login_required
def changepwd(request):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/UserApp/profile/')
		else:
			return redirect('/UserApp/changepwd/')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request,'UserApp/changePWD.html',args)


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def set_password():
	pass

def register(request):
	registered=False
	if request.method == "POST":
		user_form = forms.UserForm(data=request.POST)
		profile_form = forms.UserProfileInfoForm(data=request.POST)


		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()


			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered=True

		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = forms.UserForm()
		profile_form = forms.UserProfileInfoForm()


	return render(request,'UserApp/Register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):

	if request.method =="POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		#authentication
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Account not active")

		else:
			print("login failed")
			print("Username:{} and password {}".format(username,password))
			return HttpResponse("invalid login")

	else:
		return render(request, 'UserApp/login.html',{})
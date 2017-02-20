from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.utils.crypto import get_random_string
from .forms import UserLoginForm, UserRegisterForm
from .models import Profile
def login_view(request):
	if request.user.is_active:
		profile = Profile.objects.filter(user=request.user).first()
		key = profile.token
		return render(request, "login.html", {"key":key})
	#print request.user.is_authenticated()
	#nextp = request.GET.get("next")
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		profile = Profile.objects.filter(user=request.user).first()
		key = profile.token
		return render(request, "login.html", {"key":key})
	return render(request, "register.html", {"form":form, "title":title})


def register(request):
	#print request.user.is_authenticated()
	
	title = "Register"
	if request.method=="POST":

		form = UserRegisterForm(data=request.POST)
		#print form.is_valid()
		if form.is_valid():
			print "hi"
			user = form.save(commit=False)
			password = form.cleaned_data.get("password")
			user.set_password(password)
			user.save()
			profile = Profile()
			profile.user = user;
			token = get_random_string(length=15)
			profile.token = token
			profile.save()
			new_user = authenticate(username=user.username,password=password)
			login(request, new_user)
			# if nextp:
			# 	return redirect(nextp)
			return render(request,'register.html',{'key':token})
	form = UserRegisterForm()
	# p_form = ProfileForm()
	context = {
	'title':title,
	'form':form,
	#'p_form':p_form
	}
	return render(request, "register.html", context)

def logout_view(request):
	logout(request)
	return redirect("/accounts/login/")
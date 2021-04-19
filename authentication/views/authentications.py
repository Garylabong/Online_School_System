from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from authentication.forms import EditProfileForm
from django.contrib import messages
from django.conf import settings
from authentication.forms import PasswordChangingForm


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:T_dashboard')
        else:
            return redirect('students:S_dashboard')

    return render(request, 'home.html')

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangingForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You Have Edited Your Password...'))
			return redirect('home')
	else:
		form = PasswordChangingForm(user= request.user)

	context = {'form': form}
	return render(request, 'registration/change_password.html', context)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You Have Edited Your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance= request.user)

	context = {'form': form}
	return render(request, 'registration/edit_profile.html', context)
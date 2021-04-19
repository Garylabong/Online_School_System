from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.db import transaction

from .models import (Student, Teacher, User)

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", max_length=100, widget=forms. TextInput(attrs={'type':'hidden'}))
    email       = forms.EmailField(label="", widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name  = forms.CharField(label="", max_length=100, widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name   = forms.CharField(label="", max_length=100, widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')
        
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']        = 'form-control'
        self.fields['username'].widget.attrs['placeholder']  = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class ="form-text text-muted"><small></small></span>'

class StudentSignUpForm(UserCreationForm):
    email       = forms.EmailField(label="", widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name  = forms.CharField(label="", max_length=100, widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name   = forms.CharField(label="", max_length=100, widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2' )
 
    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']        = 'form-control'
        self.fields['username'].widget.attrs['placeholder']  = 'User Name'
        self.fields['username'].label = ''
    
        self.fields['username'].help_text = '<span class ="form-text text-muted"><small></small></span>'
        self.fields['password1'].widget.attrs['class']       = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class ="form-text text-muted"><small></small></span>'

        self.fields['password2'].widget.attrs['class']       = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class ="form-text text-muted"><small></small></span>'

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user

class TeacherSignUpForm(UserCreationForm):
    email       = forms.EmailField(label="", widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name  = forms.CharField(label="", max_length=100, widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name   = forms.CharField(label="", max_length=100, widget=forms. TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2' )
        
    def __init__(self, *args, **kwargs):
        super(TeacherSignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']        = 'form-control'
        self.fields['username'].widget.attrs['placeholder']  = 'User Name'
        self.fields['username'].label = ''
      
        self.fields['username'].help_text = '<span class ="form-text text-muted"><small></small></span>'
        self.fields['password1'].widget.attrs['class']       = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class ="form-text text-muted"><small></small></span>'

        self.fields['password2'].widget.attrs['class']       = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class ="form-text text-muted"><small></small></span>'


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_teacher = True
        if commit:
            user.save()
        return user

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget=forms. PasswordInput(attrs={'class':'form-control','placeholder': 'Old password', 'type':'password'}))
    new_password1  = forms.CharField(label="", max_length=100, widget=forms. PasswordInput(attrs={'class':'form-control','placeholder': 'New password', 'type':'password'}))
    new_password2   = forms.CharField(label="", max_length=100, widget=forms. PasswordInput(attrs={'class':'form-control','placeholder': 'New password confirmation', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')



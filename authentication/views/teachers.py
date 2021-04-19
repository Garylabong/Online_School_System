from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from ..forms import TeacherSignUpForm
from ..models import User, Subject, Course, Semester, Teacher
from .authentications import *

import uuid

def T_dashboard(request):
    return render(request, 'teachers/T_dashboard.html',{})

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:T_dashboard')

@method_decorator(login_required, name='dispatch')
class teacherAddSubjectView(CreateView):
    model = Subject
    fields = '__all__'
    template_name = 'teachers/add_subject.html'
    
    def form_valid(self, form):
        semester = form.save(commit=False)
        semester.name = self.request.user
        semester.save()
        messages.success(self.request, 'You have been Created a Subject! Go ahead now on Semester Page.')
        return redirect('teachers:add_subject')

@method_decorator(login_required, name='dispatch')
class teacherAddSemView(CreateView):
    model = Semester
    fields = '__all__'
    template_name = 'teachers/add_sem.html'
    
    def form_valid(self, form):
        course = form.save(commit=False)
        course.name = self.request.user
        course.save()
        messages.success(self.request, 'You have been Added a Sem! Go ahead now on Course Page.')
        return redirect('teachers:add_sem')

@method_decorator(login_required, name='dispatch')
class teacherAddCourseView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'teachers/add_course.html'
    
    def form_valid(self, form):
        course = form.save(commit=False)
        course.name = self.request.user
        course.save()
        messages.success(self.request, 'You have been Added a Sem! Go ahead now on Course Page.')
        return redirect('teachers:add_course')
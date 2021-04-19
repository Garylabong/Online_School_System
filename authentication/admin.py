from django.contrib import admin

# Register your models here.
from .models import User, Course, Subject, Student, Semester, Teacher

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name','email','is_student', 'is_teacher' ,'is_active')
    list_filter = ("is_student","is_teacher")
    search_fields = ['first_name', 'last_name']

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Student)
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Subject(models.Model):
    sub_name = models.CharField(max_length=30)
    sub_code = models.IntegerField()

    def __str__(self):
        return self.sub_name

class Semester(models.Model):
    sem_name = models.CharField(max_length=30)
    subject = models.ManyToManyField(Subject, related_name='+')

    def __str__(self):
        return self.sem_name

class Course(models.Model):
    course = models.CharField(max_length=30)
    semester = models.ManyToManyField(Semester, related_name='+')
    subject = models.ManyToManyField(Subject, related_name='+')


    def __str__(self):
        return self.course


# student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return self.user.username

# teacher model
class Teacher(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
    	return self.user.username
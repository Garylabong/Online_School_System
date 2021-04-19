# Online_School_System

User Authentication and Multiple User (Teacher/Student)

Repository for User Online_School_System. The app is made using Python/Django backend with SQLite3 database and also using bootstrap for frontend design.


Admin users are allowed to: 

- Admin
   - admin can assign a set of subjects per semester in a course
   - admin can assign a subject to a course
   - admin must be able to create, update, search and inactive a teacher profile
   - admin can assign teacher to any course
   - admin must be able to create, update, search and inactive a student profile
  
• Add user/remove/delete/is_student/is_teacher.

• remove user accounts etc.

• activate and deactivate user accounts (teacher/Student).


Users are allowed: 

- Teacher
     - teacher management
        - A page the teacher can see her assigned subject
        - must have a subject page where the teacher can assign her/himself -- although the Admin can
        - teacher must be able to edit his/her data
 - Student
     - student management
         - page where the student can apply for his chosen course
         - must have a Semester page where the student can see her/his Semester
         - student must be able to edit his/her data

• Register user account (Student/Teacher).

• Add for teacher environment a Subject and what Semester

• Edit Profile. 

• Change Password. 

• Login/logout user(Student/Teacher).


Installing 


*Install django (version 3.1.5)using pip:

*pip install django.

*pip freeze.

*django-admin startproject.

*py manage.py startapp.

*py manage.py createsuperuser


Start Server


py manage.py runserver Open a browser and go to http://127.0.0.1:8000

Usage django-admin manage.py python -m django



Comments: 

The backend is working, allow the user (Student/teacher) register. About the teacher profile some of are not done and have bugs and erros to fix.

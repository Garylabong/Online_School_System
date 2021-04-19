from django.urls import include, path

from .views import authentications, students, teachers
from . import views
from .views.authentications import *

urlpatterns = [

path('change_password/', authentications.change_password, name='change_password'),
path('edit_profile/',authentications.edit_profile, name="edit_profile"),
    path('', authentications.home, name='home'),

    path('students/', include(([
        path('', students.S_dashboard, name='S_dashboard'),
    ], 'authentications'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.T_dashboard, name='T_dashboard'),
        path('add_subject', teachers.teacherAddSubjectView.as_view(), name='add_subject'),
        path('add_sem', teachers.teacherAddSemView.as_view(), name='add_sem'),
    ], 'authentications'), namespace='teachers')),
]
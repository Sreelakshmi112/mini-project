from django.conf.urls import url
from stu_register import  views
urlpatterns=[
    url('reg/',views.stu_register),
    url('view_student/',views.view_student)

    ]
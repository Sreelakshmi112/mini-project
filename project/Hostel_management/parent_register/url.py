from django.conf.urls import url
from parent_register import  views

urlpatterns=[
    url('reg_parent/',views.parent_register),
    url('view_parent',views.view_parent)
   ]
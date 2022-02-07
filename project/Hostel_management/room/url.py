from django.conf.urls import url
from room import  views
urlpatterns=[
    url('view_rm/',views.room),
    ]
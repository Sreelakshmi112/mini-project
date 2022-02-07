from django.conf.urls import url
from food import  views
urlpatterns=[
    url('pst_fd/',views.post_fd),
    url('view_fd/',views.view_fd),
    ]
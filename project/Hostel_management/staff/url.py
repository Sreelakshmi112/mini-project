from django.conf.urls import url
from staff import views
urlpatterns=[
    url('post_staff/',views.poststaff),
    url('view_staff/',views.view_staff),
    url('view_staff_stu',views.view_staffs)
    ]
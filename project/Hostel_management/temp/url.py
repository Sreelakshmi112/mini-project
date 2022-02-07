from django.conf.urls import url
from temp import  views
urlpatterns=[
    url('student/',views.student_hm),
    url('admin/', views.admin_hm),
    url('login/', views.login),
    url('parent/', views.parent_hm),

]
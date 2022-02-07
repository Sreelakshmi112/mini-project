from django.conf.urls import url
from attendance import  views
urlpatterns=[
    url('post_att/(?P<idd>\w+)',views.post_att,name='post_att'),
    url('view_att/',views.view_att),
    url('view_atts/', views.view_atts)

]
from django.conf.urls import url
from vacate import  views
urlpatterns=[
    url('vacainfo/',views.vacateinfo),
    url('view_vaca/',views.view_vacate),
    url('vacated/(?P<id>\w+)',views.vacate,name='vacated')
    ]
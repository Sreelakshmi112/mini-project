from django.conf.urls import url
from rent import  views
urlpatterns=[
    url('pst_rnt/',views.post_rent),
    url('view_rnt/',views.view_rent),
    url('view_rnt_p/',views.view_rent_p)
    ]
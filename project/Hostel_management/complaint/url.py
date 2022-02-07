from django.conf.urls import url
from complaint import  views
urlpatterns=[
    url('pst_cmp/',views.post_compl),
    url('view_com/',views.view_comp),
    # url('reply/',views.reply),
    url(r'^view_rply/',views.view_rep),
    url(r'^cmp_reply/(?P<idd>\w+)',views.cmp_reply,name='cmp_reply')

]
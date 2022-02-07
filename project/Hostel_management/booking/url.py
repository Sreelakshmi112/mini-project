from django.conf.urls import url
from booking import  views
urlpatterns=[
    url('booking/',views.booking),
    url('manage_bookroom/',views.manage_bookroom),
    url('book_room/(?P<dd>\w+)',views.book,name='book_room'),
    url('accept/(?P<idd>\w+)',views.accept,name='accept'),
    url('reject/(?P<idd>\w+)',views.reject,name='reject'),
    url('dy_fee/(?P<idd>\w+)',views.dy_fee,name='dy_fee'),
    url('amount/',views.rmamount),
    # url('dy_fee/', views.dy_fee)

]
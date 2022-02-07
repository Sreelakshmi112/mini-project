from django.shortcuts import render
from booking.models import Booking
from room.models import  Room
from rent.models import Rent
# Create your views here.
def booking(request):
    ob=Room.objects.all()
    context={
        'objval':ob,
    }
    return render(request,"booking/booking.html",context)






# def room(request):
#     ob = Room.objects.all()
#     context = {
#         'value': ob
#     }
#     return render(request,"room/view_room.html",context)

def manage_bookroom(request):
    ob = Booking.objects.all()
    context = {
        'value': ob
    }
    return render(request,"booking/view_booking.html",context)


def accept(request,idd):
    obj=Booking.objects.get(id=idd)
    obj.status="accepted"
    obj.save()
    return manage_bookroom(request)


def reject(request,idd):
    obj=Booking.objects.get(id=idd)
    obj.status="rejected"
    obj.save()
    return manage_bookroom(request)


import datetime

def book(request,dd):
    mp = request.session["user_id"]
    obj=Booking()
    obj.s_id=mp
    obj.status="booking reuested"
    # print(idd)
    obj.date=datetime.datetime.today()
    obj.r_id=dd
    obj.save()
    return booking(request)



def dy_fee(request,idd):
    obj=Rent.objects.filter(id=idd)
    context={
        'obval':obj,
    }
    if request.method=="POST":
        ob=Booking.objects.get(id=idd)
        ob.no_of_days=request.POST.get('day')
        ob.no_of_room=request.POST.get('room')
        ob.status="booking reuested"
        day=request.POST.get('day')
        rm=request.POST.get('room')
        am=request.POST.get('amount')
        ob.amount=int(day)*int(rm)*int(am)
        ob.save()
        objj=Room.objects.get(id=idd)
        rm=request.POST.get('room')
        ar=objj.available_rm
        to=int(ar)-int(rm)
        objj.available_rm=to
        objj.save()
    return render(request,'booking/book_dy_fee.html',context)



def rmamount(request):
    eid=request.session["user_id"]
    objlist=Booking.objects.filter(id=eid)
    context={
        'obval':objlist
    }
    return render(request,'booking/view_rm_amount.html',context)
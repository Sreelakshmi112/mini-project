from django.shortcuts import render
from staff.models import Staff
# Create your views here.
def poststaff(request):
    if request.method == "POST":
        obj= Staff()
        obj.staff_name=request.POST.get('SNAME')
        obj.job_type=request.POST.get('JB')
        obj.phone_no=request.POST.get('PHNO')
        obj.s_id=1
        obj.save()
    return render(request,'staff/post_staff.html')


def view_staff(request):
    ob = Staff.objects.all()
    context = {
        'value': ob
    }
    return render(request,"staff/view_staffdetail.html",context)


def view_staffs(request):
    obb = Staff.objects.all()
    context = {
        'value': obb
    }
    return render(request, "staff/View_staff_std.html", context)

# Create your views here.

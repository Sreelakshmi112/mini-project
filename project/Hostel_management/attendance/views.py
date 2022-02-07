from django.shortcuts import render
from attendance.models import Attendance
# Create your views here.
def post_att(request,idd):
    if request.method=="POST":
        obj=Attendance()
        obj.month=request.POST.get('mnth')
        obj.working_days=request.POST.get('tday')
        obj.attendance=request.POST.get('pday')
        obj.student_id=idd
        obj.save()
    return render(request,"attendance/POST_ATTENDANCE.html")



def view_att(request):
    mp=str(request.session["user_id"])
    ob=Attendance.objects.filter(student_id=mp)
    context={
        'value':ob,
    }
    return render(request,"attendance/view_attendance.html",context)

def view_atts(request):
    ob=Attendance.objects.all()
    context={
        'value':ob
    }
    return render(request,"attendance/view_attendence_S.html",context)

from django.shortcuts import render
from stu_register.models import StuRegister
from login.models import Login

# Create your views here.

def stu_register(request):
    mp = request.session["user_id"]
    if request.method == "POST":
        obj= StuRegister()
        obj.name=request.POST.get('name')
        obj.password=request.POST.get('pw')
        obj.e_mail= request.POST.get('mail')
        obj.pincode = request.POST.get('pin')
        obj.city = request.POST.get('city')
        obj.address = request.POST.get('address')
        obj.department = request.POST.get('dep')
        obj.gender= request.POST.get('gender')
        obj.student_phnot=request.POST.get('c_no')
        obj.parent_id=mp
        obj.save()
        ob = Login()
        ob.user_name = request.POST.get('mail')
        ob.pass_field = request.POST.get('pw')
        ob.type = 'student'
        ob.user_id = obj.id
        ob.save()
    return render(request,"stu_register/Registration.html")


def stu_reg(request):
    return render(request,"stu_register/Registration.html")


def view_student(request):
    ob = StuRegister.objects.all()
    context = {
        'value': ob
    }
    return render(request,"stu_register/view_student.html",context)

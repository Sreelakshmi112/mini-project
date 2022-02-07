from django.shortcuts import render
from parent_register.models import ParentRegister
from login.models import Login
from django.http import HttpResponseRedirect
from stu_register.models import StuRegister


# Create your views here.
def parent_register(request):
    mp = request.session["user_id"]
    if request.method == "POST":

        ob = StuRegister()
        ob.name = request.POST.get('name')
        ob.address = request.POST.get('address')
        ob.department = request.POST.get('dep')
        ob.student_phno = request.POST.get('s_no')
        ob.e_mail = request.POST.get('smail')
        # ob.e = request.POST.get('smail')
        ob.parent_id = mp
        ob.city = request.POST.get('city')
        ob.pincode = request.POST.get('pin')
        ob.password = request.POST.get('pw')
        ob.gender=request.POST.get('gender')
        ob.save()


        obj=ParentRegister()
        obj.name = request.POST.get('pname')
        obj.address= request.POST.get('address')
        obj.phone_no =request.POST.get('s_no')
        obj.e_mail =request.POST.get('pmail')
        obj.s_id = ob.id
        obj.city = request.POST.get('city')
        obj.pincode= request.POST.get('pin')
        obj.password=request.POST.get('pw')
        obj.save()


        obb=Login()
        obb.user_name=request.POST.get('pmail')
        obb.pass_field=request.POST.get('pw')
        obb.type='parent'
        obb.user_id=obj.id

        obb.save()

        obk=Login()
        obk.user_name=request.POST.get('smail')
        obk.pass_field=request.POST.get('pw')
        obk.type='student'
        obk.user_id=ob.parent_id
        obk.save()
    return render(request,"parent_register/Registration_parent.html")

    # return HttpResponseRedirect('parent_register/reg_parent')


def view_parent(request):
    obi = ParentRegister.objects.all()
    context = {
        'value': obi
    }
    return render(request,"parent_register/view_parent.html",context)

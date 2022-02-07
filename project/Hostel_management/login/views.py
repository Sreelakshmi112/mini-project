from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        un = request.POST.get("name")
        ps = request.POST.get("pwd")
        if Login.objects.filter(user_name=un, pass_field=ps):
            obj = Login.objects.filter(user_name=un, pass_field=ps)
            tp = ""
            for l in obj:
                tp = l.type
                uid = l.user_id
                if tp == "admin":
                    request.session["user_id"] = uid
                    return render(request, 'temp/admin.html')
                    # return HttpResponseRedirect('/temp/admin/')
                elif tp == "student":
                    request.session["user_id"] = uid
                    # return HttpResponseRedirect('/temp/staff/')
                    return render(request, 'temp/student.html')
                elif tp == "parent":
                    request.session["user_id"] = uid
                    # return HttpResponseRedirect('/temp/student/')
                    return render(request, 'temp/parent.html')

        else:
            obje = "Incorrect username or password!!!"
            context = {
                'inv': obje,
            }
            return render(request, 'login/login.html', context)
    return render(request,"login/login.html")
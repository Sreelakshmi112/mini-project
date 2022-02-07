from django.shortcuts import render
from  vacate.models import Vacate
# Create your views here.
def vacateinfo(request):
    if request.method == "POST":
        obj= Vacate()
        obj.date=request.POST.get('date')
        obj.s_id=1
        obj.save()
    return render(request,"vacate/vacateifo.html")


def view_vacate(request):
    ob = Vacate.objects.all()
    context = {
        'value': ob
    }
    return render(request,"vacate/view_vacate.html",context)



def vacate(request,id):
    obj=Vacate.objects.get(id=id)
    obj.status="Vacated"
    obj.save()
    return view_vacate(request)

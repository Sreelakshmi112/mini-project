from django.shortcuts import render
from rent.models import Rent
# Create your views here.
def post_rent(request):
    if request.method == "POST":
        obj=Rent()
        obj.days=request.POST.get('day')
        obj.fees=request.POST.get('fee')
        obj.save()
    return render(request,"rent/post_fees.html")


def view_rent(request):
    ob = Rent.objects.all()
    context = {
        'value': ob
    }
    return render(request,"rent/View_rent.html",context)



def view_rent_p(request):
    ob = Rent.objects.all()
    context = {
        'value': ob
    }
    return render(request,"rent/view_rent_p.html",context)



from django.shortcuts import render
from food.models import Food
# Create your views here.
def post_fd(request):
    if request.method=="POST":
        obj=Food()
        obj.day=request.POST.get('day')
        obj.breakfast=request.POST.get('BF')
        obj.lunch=request.POST.get('LU')
        obj.dinner=request.POST.get('DI')
        obj.save()
    return render(request,"food/POST_FOODMENUE.html")

def view_fd(request):
    ob = Food.objects.all()
    context = {
        'value': ob
    }
    return render(request,"food/View_food.html",context)





from django.shortcuts import render
from complaint.models import Complaint
# Create your views here.
def post_compl(request):
    mp=request.session["user_id"]
    if request.method=="POST":
        obj=Complaint()
        obj.complaint=request.POST.get('cmp')
        # obj.reply='pending'
        obj.student_id=mp
        obj.save()
    return render(request,"complaint/post_complaint.html")



def reply(request):
    # if request.method == "POST":
    #     obj = Complaint()
    #     # obj.complaint = request.POST.get('cmp')
    #     obj.reply=request.POST.get('rp')
    return render(request,"complaint/replay.html")


def view_rep(request):
    ob = Complaint.objects.all()
    context = {
        'value': ob
    }
    return render(request,"complaint/view_reply.html",context)


def view_comp(request):
    ob = Complaint.objects.all()
    context = {
        'value': ob,
    }
    return render(request,"complaint/View_complaint.html",context)


def cmp_reply(request,idd):
    # ob=Complaint.objects.filter(c_id=abc)
    # context={
    #     'val':ob,
    # }
    if request.method=="POST":
        obj=Complaint.objects.get(c_id=idd)
        obj.reply=request.POST.get('rep')
        obj.save()
        # return view_comp(request)
    return render(request,'complaint/replay.html')

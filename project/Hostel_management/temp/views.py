from django.shortcuts import render

# Create your views here.
def admin_hm(request):
    return  render(request,"temp/admin.html")


def login(request):
    return  render(request,"temp/login.html")

def student_hm(request):
    return  render(request,"temp/student.html")

def parent_hm(request):
    return  render(request,"temp/parent.html")






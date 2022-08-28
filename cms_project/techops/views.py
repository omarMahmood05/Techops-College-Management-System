from django.shortcuts import render
from django.http import HttpResponse
from techops.models import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def techops_login(request):
    return render(request, 'techops_login_page.html')

def student_login(request):
    student_email=request.POST.get('student_email')
    student_password=request.POST.get('student_password')
    try:
        if student.objects.filter(student_email=student_email,student_password=student_password).exists():
            return render(request, 'dashboard.html')
        else:
            return render(request,'techops_login_page_failed.html')
    except:
         return render(request,'techops_login_page_failed.html')

def techops_login_page_failed(request):
    return render(request, 'techops_login_page_failed.html')


def techops_signup(request):
    return render(request, 'techops_signup_page.html')

def techops_dashboard(request):
    return render(request, 'dashboard.html')

def techops_results(request):
    return render(request, 'techops_results.html')

def techops_feesPayment(request):
    return render(request, 'techops_feesPayment.html')

def techops_admit_card(request):
    return render(request, 'techops_admit_card.html')

def faculty_login_page(request):
    return render(request, 'faculty_login_page.html')

def techops_backlogs(request):
    return render(request, 'techops_backlogs.html')

def techops_profile(request):
    return render(request, 'techops_profile.html')

def faculty_add_student(request):
    return render(request, 'faculty_add_student.html')

def add_student_submit(request):
    x = student()
    try:
        x.student_name=request.POST.get('student_name')
        x.student_fathername=request.POST.get('father_name')
        x.student_mothername=request.POST.get('mother_name')
        x.student_email=request.POST.get('student_email')
        x.student_phoneno=request.POST.get('student_phno')
        x.student_dob=request.POST.get('student_dob')
        x.student_password=request.POST.get('student_password')
        x.save()
        return render(request,'dashboard.html')
    except Exception as e:
        return HttpResponse(e)

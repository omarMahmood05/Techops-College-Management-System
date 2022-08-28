from django.shortcuts import render
from django.http import HttpResponse
from techops.models import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def techops_login(request):
    return render(request, 'techops_login_page.html')

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


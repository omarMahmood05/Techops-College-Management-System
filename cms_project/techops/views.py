from django.shortcuts import render
from django.http import HttpResponse
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
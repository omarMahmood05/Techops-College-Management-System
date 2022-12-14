from django.shortcuts import render, redirect
from django.http import HttpResponse
from techops.models import *
from techops.forms import *
# Create your views here.

student_authenticated = False
userName = ''
faculty_authenticated = False
admin_authenticated = False

def homepage(request):
    student_authenticated = False
    faculty_authenticated = False
    admin_authenticated = False

    return render(request, 'homepage.html')

def techops_login(request):
    return render(request, 'techops_login_page.html')

def student_login(request):
    student_email=request.POST.get('student_email')
    student_password=request.POST.get('student_password')
    try:
        if student.objects.filter(student_email=student_email,student_password=student_password).exists():
            global student_authenticated
            student_authenticated = True
            stu = student.objects.get(student_email = student_email)
            context = {'user': stu}
            global userName
            userName = student_email
            return render(request, 'dashboard.html', context)
        else:
            return render(request,'techops_login_page_failed.html')
    except:
         return render(request,'techops_login_page_failed.html')

def student_log_out(request):
    global student_authenticated
    student_authenticated = False
    userName = ''
    faculty_authenticated = False
    admin_authenticated = False
    return render(request, 'homepage.html')

def authentication_error(request):
    return render(request, 'authentication_error.html')

def techops_login_page_failed(request):
    global student_authenticated
    student_authenticated = False
    return render(request, 'techops_login_page_failed.html')

def techops_signup(request):
    return render(request, 'techops_signup_page.html')

# STUDENT PAGES
def techops_dashboard(request):
    if student_authenticated:
        student_email = userName
        stu = student.objects.get(student_email = student_email)
        context = {'user': stu}
        return render(request, 'dashboard.html', context)
    else: 
        return render(request, 'authentication_error.html')

def techops_results(request):
    if student_authenticated:
        student_email = userName
        stu = student.objects.get(student_email = student_email)
        result = results.objects.all()
        context = {'user': stu, 'result' : result}
        return render(request, 'techops_results.html', context)
    else: 
        return render(request, 'authentication_error.html')

def techops_feesPayment(request):
    if student_authenticated:
        student_email = userName
        stu = student.objects.get(student_email = student_email)
        context = {'user': stu}
        return render(request, 'techops_feesPayment.html', context)
    else: 
        return render(request, 'authentication_error.html')
    
def techops_admit_card(request):
    if student_authenticated:
        student_email = userName
        stu = student.objects.get(student_email = student_email)
        context = {'user': stu}
        return render(request, 'techops_admit_card.html', context)
    else: 
        return render(request, 'authentication_error.html')

def techops_backlogs(request):
    if student_authenticated:
        student_email = userName
        stu = student.objects.get(student_email = student_email)
        context = {'user': stu}
        return render(request, 'techops_backlogs.html', context)
    else: 
        return render(request, 'authentication_error.html')

def techops_profile(request):
    return render(request, 'techops_profile.html')

# Faculty Pages

def faculty_login_page(request):
    return render(request, 'faculty_login_page.html')

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
        return redirect('./faculty_list_student')
    except Exception as e:
        return HttpResponse(e)

def admin_login_page(request):
    return render(request, 'admin_login_page.html')

def admin_login(request):
    admin_email_c = "admin@techops.com"
    admin_pass_c = "admin"
    admin_email = request.POST.get('admin_email')
    admin_pass = request.POST.get('admin_password')
    try:
        if admin_email_c == admin_email:
            if admin_pass_c == admin_pass:
                return render(request, 'admin_dashboard.html')
            else:
                return render(request, 'homepage.html')
        else:
            return render(request, 'homepage.html')
    except:
        return render(request, 'homepage.html')

def admin_add_faculty(request):
    return render(request, 'admin_add_faculty.html')

def admin_manage_faculty(request):
    return render(request, 'admin_manage_faculty.html')

def admin_list_faculty(request):
    f = faculty.objects.all()
    context = {'facultyMembers': f}
    return render(request, 'admin_list_faculty.html', context)


def add_faculty_submit(request):
    y=faculty()
    try:
        y.faculty_name=request.POST.get('faculty_name')
        y.faculty_email=request.POST.get('faculty_email')
        y.faculty_status=request.POST.get('faculty_status')
        y.faculty_password=request.POST.get('faculty_password')
        y.save()
        return redirect('./admin_list_faculty')
        # return render(request, 'admin_list_faculty.html')
    except Exception as e:
        return HttpResponse(e)


def faculty_member_delete(request,id):
    f = faculty.objects.get(id=id)
    f.delete()
    return redirect('../admin_list_faculty')

def admin_faculty_edit(request, id):
    f = faculty.objects.get(id = id)
    context = {'member': f}
    return render(request, 'admin_faculty_edit.html', context)

        # f_form = edited_form(request.POST, instance = f)
        # try:
        #     f_form.save()
        #     return redirect('../admin_list_faculty')        
        # except Exception as e:
        #     return HttpResponse(e)   

def faculty_login(request):
    faculty_email=request.POST.get('faculty_email')
    faculty_password=request.POST.get('faculty_password')
    try:
        if faculty.objects.filter(faculty_email=faculty_email,faculty_password=faculty_password).exists():
            global faculty_authenticated
            faculty_authenticated = True
            return render(request, 'faculty_dashboard.html')
        else:
            return render(request,'faculty_login_page_error.html')
    except:
         return render(request,'faculty_login_page_error.html')

def faculty_results(request):
    return render(request, 'faculty_results.html')

def faculty_manage_student(request):
    return render(request, 'faculty_manage_student.html')

def faculty_list_student(request):
    stu = student.objects.all()
    context = {'students': stu}
    return render(request, 'faculty_list_student.html', context)


def faculty_student_delete(request,id):
    stu = student.objects.get(id=id)
    stu.delete()
    return redirect('../faculty_list_student')

def faculty_student_edit(request, id):
    stu = student.objects.get(id = id)
    context = {'student': stu}
    return render(request, 'faculty_student_edit.html', context)

def student_edited(request, id):
    stu = student.objects.get(id = id)
    newFatherName = request.POST.get('father_name')
    newMotherName = request.POST.get('mother_name')
    newPassword = request.POST.get('student_password')
    newPhoneNumber = request.POST.get('student_phno')
    stu.student_fathername = newFatherName
    stu.student_mothername = newMotherName
    stu.student_password = newPassword
    stu.student_phoneno = newPhoneNumber
    stu.save()
    return redirect('../faculty_list_student')

def faculty_edited(request,id):
    f = faculty.objects.get(id=id)
    newStatus = request.POST.get('faculty_status')
    newPassword = request.POST.get('faculty_password')
    f.faculty_status = newStatus
    f.faculty_password = newPassword
    f.save()
    return redirect('../admin_list_faculty')

def add_results(request, id):
    context = {'id': id}
    return render(request, './student_result_submit.html', context)

def student_add_results_submit(request):
    x = results()
    try:
        x.student_id = request.POST.get('student_id')
        x.subject_name = request.POST.get('subject_name')
        x.subject_grade = request.POST.get('subject_grade')
        x.subject_marks = request.POST.get('subject_marks')
        x.save()
        return redirect('./faculty_list_student')
    except Exception as e:
        return HttpResponse(e)

def faculty_student_results(reqeust):
    res = results.objects.all()
    context = {'result': res}
    return render(reqeust, 'faculty_student_results.html', context)

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
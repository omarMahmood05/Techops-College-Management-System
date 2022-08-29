from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    # Student URLs
    path('techops_login_page', views.techops_login),
    path('techops_login_page_failed', views.techops_login_page_failed),
    path('student_log_out', views.student_log_out),
    path('authentication_error', views.authentication_error),
        # Error Login 
    path('student_login', views.student_login),
    # Signup Page
    path('techops_signup_page', views.techops_signup),
    # Inner Contents - Student
    path('techops_dashboard', views.techops_dashboard),
    path('techops_results', views.techops_results),
    path('techops_feesPayment', views.techops_feesPayment),
    path('techops_admit_card', views.techops_admit_card),
    path('techops_backlogs', views.techops_backlogs),
    path('techops_profile', views.techops_profile),
    # Faculty URLs
    path('faculty_login_page', views.faculty_login_page),
    path('faculty_login', views.faculty_login),
    path('faculty_add_student', views.faculty_add_student),
    path('add_student_submit', views.add_student_submit),
    path('faculty_results', views.faculty_results),
    path('faculty_manage_student', views.faculty_manage_student),
    path('faculty_list_student', views.faculty_list_student),
    # Admin Pages
    path('admin_login_page', views.admin_login_page),
    path('admin_login', views.admin_login),
    path('admin_add_faculty', views.admin_add_faculty),
    path('admin_manage_faculty', views.admin_manage_faculty),
    path('admin_list_faculty', views.admin_list_faculty),
    path('add_faculty_submit', views.add_faculty_submit),
    path('faculty_member_delete/<int:id>', views.faculty_member_delete),
    path('admin_faculty_edit/<int:id>', views.admin_faculty_edit),
    path('faculty_edited/<int:id>', views.faculty_edited),
    # Testing

]
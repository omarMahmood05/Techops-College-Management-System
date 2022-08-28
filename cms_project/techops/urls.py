from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    # Student URLs
    path('techops_login_page', views.techops_login),
    path('techops_login_page_failed', views.techops_login_page_failed),
    path('techops_forgot_password', views.techops_forgot_password),
    path('reset_password', views.reset_password),
    path('student_login', views.student_login),
    path('techops_signup_page', views.techops_signup),
    path('techops_dashboard', views.techops_dashboard),
    path('techops_results', views.techops_results),
    path('techops_feesPayment', views.techops_feesPayment),
    path('techops_admit_card', views.techops_admit_card),
    path('techops_backlogs', views.techops_backlogs),
    path('techops_profile', views.techops_profile),
    # Faculty URLs
    path('faculty_login_page', views.faculty_login_page),
    path('faculty_add_student', views.faculty_add_student),
    path('add_student_submit', views.add_student_submit),
    path('admin_login_page', views.admin_login_page),
    path('admin_login', views.admin_login),
    path('admin_add_faculty', views.admin_add_faculty),
    path('admin_manage_faculty', views.admin_manage_faculty),
    path('admin_list_faculty', views.admin_list_faculty),
    # Testing

]
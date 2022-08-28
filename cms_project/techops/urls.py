from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    # Student URLs
    path('techops_login_page', views.techops_login),
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
    # Testing

]
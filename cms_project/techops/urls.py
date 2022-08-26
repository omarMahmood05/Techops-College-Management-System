from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('techops_login_page', views.techops_login),
    path('techops_signup_page', views.techops_signup),
    path('techops_dashboard', views.techops_dashboard),
    path('techops_results', views.techops_results),
]
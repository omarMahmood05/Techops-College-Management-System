from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('techops_login', views.techops_login),
    path('techops_signup', views.techops_signup),
    path('techops_dashboard', views.techops_dashboard),
]
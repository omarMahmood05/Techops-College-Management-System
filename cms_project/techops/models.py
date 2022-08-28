from django.db import models

# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=50)
    student_fathername=models.CharField(max_length=50)
    student_mothername=models.CharField(max_length=50)
    student_email=models.EmailField(max_length=50)
    student_phoneno=models.IntegerField()
    student_dob=models.DateField(max_length=50)
    student_password=models.CharField(max_length=50)
    student_picture=models.CharField(max_length=255)

class faculty(models.Model):
    faculty_name=models.CharField(max_length=50)
    faculty_email=models.EmailField(max_length=50)
    faculty_status=models.CharField(max_length=50)
    faculty_password=models.CharField(max_length=50)
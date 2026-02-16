from django.db import models




class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    agg = models.IntegerField()
    blood_group = models.CharField(max_length=100, default=" ")
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)



class User(models.Model):
    u_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default =True)
    otp = models.IntegerField(default=0)
    v_status = models.IntegerField(default=0)
    password = models.CharField(max_length=100)
    
   
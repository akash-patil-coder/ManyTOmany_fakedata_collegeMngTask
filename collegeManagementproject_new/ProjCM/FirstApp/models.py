from django.db import models

# Create your models here.
class Department(models.Model):
    dept_Name = models.CharField(max_length=40,unique=True)
    intake = models.IntegerField()

    def __str__(self):
        return f"{self.dept_Name} "

class Professor(models.Model):
    department = models.ManyToManyField(Department,related_name='department_prof')
    prof_name = models.CharField(max_length=50)
    sal = models.FloatField()

    def __str__(self):
        return self.prof_name

class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE ,related_name='department_stud')
    roll_no = models.IntegerField(unique=True)
    stud_name = models.CharField(max_length=80)
    marks = models.FloatField()

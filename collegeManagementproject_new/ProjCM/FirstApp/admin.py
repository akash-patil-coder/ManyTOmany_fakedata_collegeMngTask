from django.contrib import admin
from .models import Professor,Department,Student

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','dept_Name','intake']
admin.site.register(Department,DepartmentAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['id','prof_name','sal']
admin.site.register(Professor,ProfessorAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','roll_no','stud_name','marks']
admin.site.register(Student,StudentAdmin)
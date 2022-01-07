from django.shortcuts import render,redirect
from .models import Student,Professor,Department
from .forms import DepartmentModelForm,ProfessorModelForm,StudentModelForm

# Create your views here.

# views for Department

def AddDeptView(request):
    form = DepartmentModelForm()
    if request.method == 'POST':
        form = DepartmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Show-Dept')
    template_name = 'FirstApp/addDept.html'
    context = {'form':form}
    return render(request, template_name, context)


def ShowDeptView(request):
    dept_object = Department.objects.all()
    if request.method == 'POST':
        department = Department.objects.filter(dept_Name__icontains=request.POST['searchdata'])
        print(department)
        professor = department[0].department_prof.all()
        print(professor)
        student = department[0].department_stud.all()
        print(student)
        template_name = "FirstApp/searchDept.html"
        context = {'department': department, 'professor': professor, 'student': student}
        return render(request, template_name, context)
    template_name = 'FirstApp/showDept.html'
    context = {'dept_object': dept_object}
    return render(request, template_name, context)

def updateDeptView(request,id):
    dept_object = Department.objects.get(id=id)
    form = DepartmentModelForm(instance=dept_object)
    if request.method == 'POST':
        form = DepartmentModelForm(request.POST,instance=dept_object)
        if form.is_valid():
            form.save()
            return redirect('Show-Dept')
    template_name = 'FirstApp/addDept.html'
    context = {'form':form}
    return render(request, template_name, context)


def deleteDeptView(request,id):
    dept_object = Department.objects.get(id=id)
    if request.method == 'POST':
        dept_object.delete()
        return redirect('Show-Dept')
    template_name = 'FirstApp/deleteDept.html'
    context = {'dept_object':dept_object}
    return render(request, template_name, context)





# views for Professor





def AddProfView(request):
    form = ProfessorModelForm()
    if request.method == 'POST':
        form = ProfessorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Show-Prof')
    template_name = 'FirstApp/addProf.html'
    context = {'form':form}
    return render(request, template_name, context)

def ShowProfView(request):
    prof_object = Professor.objects.all()
    if request.method == 'POST':
        prof_object = Professor.objects.filter(prof_name__icontains=request.POST['searchdata'])
    template_name = 'FirstApp/showProf.html'
    context = {'prof_object': prof_object}
    return render(request, template_name, context)


def updateProfView(request,id):
    prof_object = Professor.objects.get(id=id)
    form = ProfessorModelForm(instance=prof_object)
    if request.method == 'POST':
        form = ProfessorModelForm(request.POST,instance=prof_object)
        if form.is_valid():
            form.save()
            return redirect('Show-Prof')
    template_name = 'FirstApp/addProf.html'
    context = {'form':form}
    return render(request, template_name, context)


def deleteProfView(request,id):
    prof_object = Professor.objects.get(id=id)
    if request.method == 'POST':
        prof_object.delete()
        return redirect('Show-Prof')
    template_name = 'FirstApp/deleteProf.html'
    context = {'prof_object':prof_object}
    return render(request, template_name, context)

def DetailsProfView(request,id):
    prof_object = Student.objects.filter(roll_no=id)
    prof_object_1 = Professor.department.through.objects.all()
    template_name = 'FirstApp/detailStud.html'
    context = {'prof_object': prof_object,'prof_object_1':prof_object_1}
    return render(request, template_name, context)



# views for Student



def AddStudView(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Show-Stud')
    template_name = 'FirstApp/addStud.html'
    context = {'form':form}
    return render(request, template_name, context)


def ShowStudView(request):
    stud_object = Student.objects.all()
    if request.method == 'POST':
        stud_object = Student.objects.filter(stud_name__icontains=request.POST['searchdata'])
    template_name = 'FirstApp/showStud.html'
    context = {'stud_object': stud_object}
    return render(request, template_name, context)


def updateStudView(request,id):
    stud_object = Student.objects.get(roll_no=id)
    form = StudentModelForm(instance=stud_object)
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=stud_object)
        if form.is_valid():
            form.save()
            return redirect('Show-Stud')
    template_name = 'FirstApp/addStud.html'
    context = {'form':form}
    return render(request, template_name, context)


def deleteStudView(request,id):
    stud_object = Student.objects.get(roll_no=id)
    if request.method == 'POST':
        stud_object.delete()
        return redirect('Show-Stud')
    template_name = 'FirstApp/deleteStud.html'
    context = {'stud_object':stud_object}
    return render(request, template_name, context)

def DetailsStudView(request,id):
    stud_object = Student.objects.get(roll_no=id)
    template_name = 'FirstApp/detailStud.html'
    context = {'stud_object': stud_object}
    return render(request, template_name, context)






















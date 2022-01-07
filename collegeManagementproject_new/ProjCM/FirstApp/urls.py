from django.urls import path
from . import views


urlpatterns = [
    path('addDept/',views.AddDeptView,name='Add-Dept'),
    path('showDept/',views.ShowDeptView,name='Show-Dept'),
    path('updateDept/<int:id>/',views.updateDeptView,name='update_dept'),
    path('deleteDept/<int:id>/',views.deleteDeptView,name='Delete_dept'),

    path('addProf/',views.AddProfView,name='Add-Prof'),
    path('showProf/',views.ShowProfView,name='Show-Prof'),
    path('updateProf/<int:id>/',views.updateProfView,name='update_prof'),
    path('deleteProf/<int:id>/',views.deleteProfView,name='Delete_prof'),


    path('addStud/',views.AddStudView,name='Add-Stud'),
    path('showShow/',views.ShowStudView,name='Show-Stud'),
    path('updateStud/<int:id>/',views.updateStudView,name='update_stud'),
    path('deleteStud/<int:id>/',views.deleteStudView,name='Delete_stud'),
    path('detailStud/<int:id>/',views.DetailsStudView,name='Details_stud'),
]
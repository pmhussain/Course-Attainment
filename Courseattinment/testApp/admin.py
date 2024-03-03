from django.contrib import admin
from .models import *
# Register your models here.
class COAdmin(admin.ModelAdmin):
    list_display = ['co', 'description',]

class POAdmin(admin.ModelAdmin):
    list_display = ['po', 'description',]

class PSOAdmin(admin.ModelAdmin):
    list_display = ['pso', 'description',]

class IndirectAdmin(admin.ModelAdmin):
    list_display = ['co', 'high', 'medium', 'low', 'attainment']

class CO_POAdmin(admin.ModelAdmin):
    list_display = ['co', 'pos_mapped',]

class CO_PO_MatrixAdmin(admin.ModelAdmin):
    list_display = ['co', 'po1','po2','po3','po4','po5','po6','po7','po8','po9','po10','po11','po12','pso1','pso2','pso3']


class Mid1_QPAdmin(admin.ModelAdmin):
    list_display = ['question', 'co_mapped','attainment_level']
class Mid2_QPAdmin(admin.ModelAdmin):
    list_display = ['question', 'co_mapped', 'attainment_level']

class Internal_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'cos_mapped', 'attainment_level']
class External_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'cos_mapped', 'attainment_level']
class Course_AttainmentAdmin(admin.ModelAdmin):
    list_display = ['co', 'internal', 'external','direct','indirect','final']
class PO_AttainmentAdmin(admin.ModelAdmin):
    list_display = ['po', 'attainment']
class PSO_AttainmentAdmin(admin.ModelAdmin):
    list_display = ['pso', 'attainment']

admin.site.register(CO,COAdmin)
admin.site.register(PO,POAdmin)
admin.site.register(PSO,PSOAdmin)
admin.site.register(Indirect,IndirectAdmin)
admin.site.register(CO_PO_mapping,CO_POAdmin)
admin.site.register(CO_PO_Matrix,CO_PO_MatrixAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
admin.site.register(Person,PersonAdmin)
admin.site.register(StudentMark)
admin.site.register(Student_Mark)
admin.site.register(Mid1_QP,Mid1_QPAdmin)
admin.site.register(Mid2_QP,Mid2_QPAdmin)
admin.site.register(Intenal_Question,Internal_QuestionAdmin)
admin.site.register(External_Question, External_QuestionAdmin)
admin.site.register(Course_Attainment,Course_AttainmentAdmin)
admin.site.register(PO_Attainment,PO_AttainmentAdmin)
admin.site.register(PSO_Attainment,PSO_AttainmentAdmin)


#***********************
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'rollno']
class QP_mid1Admin(admin.ModelAdmin):
    list_display = ['question', 'co_mapped']
class QP_mid2Admin(admin.ModelAdmin):
    list_display = ['question', 'co_mapped']
class Mid1Admin(admin.ModelAdmin):
    list_display = ['student', 'question', 'marks' ]
class Mid2Admin(admin.ModelAdmin):
    list_display = ['student', 'question', 'marks' ]
class SEEAdmin(admin.ModelAdmin):
    list_display = ['student', 'marks']

admin.site.register(Student, StudentAdmin)
admin.site.register(QP_mid1, QP_mid1Admin)
admin.site.register(QP_mid2, QP_mid2Admin)
admin.site.register(Mid1, Mid1Admin)
admin.site.register(Mid2, Mid2Admin)
admin.site.register(SEE, SEEAdmin)

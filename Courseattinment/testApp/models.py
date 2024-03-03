from django.db import models

# Create your models here.
class CO(models.Model):
    cos = (('-','-'), ('CO1', 'CO1'), ('CO2', 'CO2'), ('CO3', 'CO3'), ('CO4', 'CO4'), ('CO5', 'CO5'), ('CO6', 'CO6'),)
    co = models.CharField(max_length=500, choices=cos, default='-')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.co

class PO(models.Model):
    pos = (('-','-'), ('PO1', 'PO1'), ('PO2', 'PO2'), ('PO3', 'PO3'), ('PO4', 'PO4'), ('PO5', 'PO5'), ('PO6', 'PO6'),
                       ('PO7', 'PO7'), ('PO8', 'PO8'), ('PO9', 'PO9'), ('PO10', 'PO10'), ('PO11', 'PO11'), ('PO12', 'PO12'),)
    po = models.CharField(max_length=500,choices=pos, default='-')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.po

class PSO(models.Model):
    pso = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.pso

class Mid1_QP(models.Model):
    question =  models.CharField(max_length=200)
    co_mapped = models.ForeignKey(CO, on_delete=models.CASCADE)
    attainment_level =models.IntegerField(default=0)
    def __str__(self):
        return self.question

class Mid2_QP(models.Model):
    question =  models.CharField(max_length=200)
    co_mapped = models.ForeignKey(CO, on_delete=models.CASCADE)
    attainment_level =models.IntegerField(default=0)
    def __str__(self):
        return self.question


class Indirect(models.Model):
    co = models.ForeignKey(CO, on_delete=models.CASCADE)
    high= models.IntegerField(null=True, default=0)
    medium = models.IntegerField(null=True, default=0)
    low = models.IntegerField(null=True, default=0)
    attainment = models.FloatField(null=True, default=0 )
    def __srt__(self):
        return self.attainment

class Course_Attainment(models.Model):
    co = models.ForeignKey(CO, on_delete=models.CASCADE)
    internal = models.FloatField(null=True, default=0)
    external = models.FloatField(null=True, default=0)
    direct = models.FloatField(null=True, default=0)
    indirect = models.ForeignKey(Indirect, on_delete=models.CASCADE)
    final = models.FloatField(null=True, default=0)

class PO_Attainment(models.Model):
    po = models.ForeignKey(PO, on_delete=models.CASCADE)
    attainment =models.FloatField(null=True, default=0)
    def __str__(self):
        return self.po.po

class PSO_Attainment(models.Model):
    pso = models.ForeignKey(PSO, on_delete=models.CASCADE)
    attainment =models.FloatField(null=True, default=0)
    def __str__(self):
        return self.pso.pso


class CO_PO_mapping(models.Model):
    co = models.ForeignKey(CO, on_delete=models.CASCADE)
    po_mapped = models.ManyToManyField(PO)

    def pos_mapped(self):
        return ",".join([str(p) for p in self.po_mapped.all()])

    def __str__(self):
        return self.co.co



class CO_PO_Matrix(models.Model):
    co = models.ForeignKey(CO, on_delete=models.CASCADE)
    levels = (
    ('-', 0),
    ('1',1),
    ('2',2),
    ('3',3),
    )
    po1 = models.CharField(max_length=10, choices=levels, default='-')
    po2 = models.CharField(max_length=10, choices=levels, default='-')
    po3 = models.CharField(max_length=10, choices=levels, default='-')
    po4 = models.CharField(max_length=10, choices=levels, default='-')
    po5 = models.CharField(max_length=10, choices=levels, default='-')
    po6 = models.CharField(max_length=10, choices=levels, default='-')
    po7 = models.CharField(max_length=10, choices=levels, default='-')
    po8 = models.CharField(max_length=10, choices=levels, default='-')
    po9 = models.CharField(max_length=10, choices=levels, default='-')
    po10 = models.CharField(max_length=10, choices=levels, default='-')
    po11 = models.CharField(max_length=10, choices=levels, default='-')
    po12 = models.CharField(max_length=10, choices=levels, default='-')
    pso1 = models.CharField(max_length=10, choices=levels, default='-')
    pso2 = models.CharField(max_length=10, choices=levels, default='-')
    pso3 = models.CharField(max_length=10, choices=levels, default='-')

    def __str__(self):
        return self.co.co


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Intenal_Question(models.Model):
    question =  models.CharField(max_length=200)
    co_mapped = models.ManyToManyField(CO)
    attainment_level =models.IntegerField(default=0)
    def cos_mapped(self):
        return ",".join([str(co) for co in self.co_mapped.all()])
    def __str__(self):
        return self.question

class External_Question(models.Model):
    question =  models.CharField(max_length=200)
    co_mapped = models.ManyToManyField(CO)
    attainment_level =models.IntegerField(default=0)
    def cos_mapped(self):
        return ",".join([str(co) for co in self.co_mapped.all()])
    def __str__(self):
        return self.question

class StudentMark(models.Model):
    rollno = models.CharField(max_length=50)
    m1_q1_marks = models.FloatField(null=True, default=None)
    m1_q2_marks = models.FloatField(null=True, default=None)
    m1_q3_marks = models.FloatField(null=True, default=None)
    m1_q4_marks = models.FloatField(null=True, default=None)
    m1_objective_marks = models.FloatField(null=True, default=None)
    m1_assignment_marks = models.FloatField(null=True, default=None)

    m2_q1_marks = models.FloatField(null=True, default=None)
    m2_q2_marks = models.FloatField(null=True, default=None)
    m2_q3_marks = models.FloatField(null=True, default=None)
    m2_q4_marks = models.FloatField(null=True, default=None)
    m2_objective_marks = models.FloatField(null=True, default=None)
    m2_assignment_marks = models.FloatField(null=True, default=None)

    ext_marks = models.FloatField(null=True, default=None)

class Student_Mark(models.Model):
    rollno = models.CharField(max_length=50)
    mid1 = models.ForeignKey(Mid1_QP,on_delete=models.CASCADE)
    mid2 = models.ForeignKey(Mid2_QP,on_delete=models.CASCADE)
    # ext = models.ForeignKey(Mid1_QP,on_delete=models.CASCADE)
    ext = models.FloatField(null=True, default=None)
    # m1_q1_marks = models.FloatField(null=True, default=None)
    # m1_q2_marks = models.FloatField(null=True, default=None)
    # m1_q3_marks = models.FloatField(null=True, default=None)
    # m1_q4_marks = models.FloatField(null=True, default=None)
    # m1_objective_marks = models.FloatField(null=True, default=None)
    # m1_assignment_marks = models.FloatField(null=True, default=None)
    #
    # m2_q1_marks = models.FloatField(null=True, default=None)
    # m2_q2_marks = models.FloatField(null=True, default=None)
    # m2_q3_marks = models.FloatField(null=True, default=None)
    # m2_q4_marks = models.FloatField(null=True, default=None)
    # m2_objective_marks = models.FloatField(null=True, default=None)
    # m2_assignment_marks = models.FloatField(null=True, default=None)
    #
    # ext_marks = models.FloatField(null=True, default=None)

    def __str__(self):
        return self.rollno


#*************************************************************
class Student(models.Model):
    name = models.CharField(max_length=100, default='XXXX')
    rollno = models.CharField(max_length=20)

    def __self__(self):
        return self.rollno

class QP_mid1(models.Model):
    question =  models.CharField(max_length=200)
    co_mapped = models.ForeignKey(CO, on_delete=models.CASCADE)
    def __str__(self):
        return self.question

class QP_mid2(models.Model):
    question =  models.CharField(max_length=200)
    co_mapped = models.ForeignKey(CO, on_delete=models.CASCADE)
    def __str__(self):
        return self.question

class Mid1(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    question = models.ForeignKey(QP_mid1,on_delete=models.CASCADE)
    marks = models.FloatField(null=True, default=None)

    def __self__(self):
        return self.student.rollno

class Mid2(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    question = models.ForeignKey(QP_mid2,on_delete=models.CASCADE)
    marks = models.FloatField(null=True, default=None)

    def __self__(self):
        return self.student.rollno


class SEE(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    marks = models.FloatField(null=True, default=None)

    def __self__(self):
        return self.student.rollno

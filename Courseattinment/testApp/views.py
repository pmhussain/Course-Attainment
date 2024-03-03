from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Avg, Sum,Count
# Create your views here.
def homee(request):
    return render (request, 'testApp/homee.html')

def add_co(request):
    cos = CO.objects.all()
    if request.method == 'POST':
        co = request.POST.get('co')
        description = request.POST.get('description')
        if CO.objects.filter(co=co).exists():
            messages.warning(request, co + " is already entered")
            return redirect('add_co')
        else:
            co = CO.objects.create(co=co,description=description)
            co.save()
            messages.success(request, co.co + " is Saved Successfully")
            return redirect('add_co')
    return render (request, 'testApp/add_co.html', locals())

def view_co(request):
    cos = CO.objects.all()
    return render (request, 'testApp/view_co.html', locals())

def edit_co(request,id):
    get_co = CO.objects.get(id=id)
    if request.method == 'POST':
        co = request.POST.get('co')
        description = request.POST.get('description')
        get_co.co=co
        get_co.description=description
        get_co.save()
        messages.success(request, get_co.co + " is updated Successfully")
        return redirect('add_co')
    return render (request, 'testApp/edit_co.html', locals())

def delete_co(request, id):
    get_co = CO.objects.get(id=id)
    get_co.delete()
    return redirect('add_co')
    return render (request, 'testApp/delete_co.html', locals())

def add_po(request):
    pos = PO.objects.all()
    if request.method == 'POST':
        po = request.POST.get('po')
        description = request.POST.get('description')
        if PO.objects.filter(po=po).exists():
            messages.warning(request, po + " is already entered")
            return redirect('add_po')
        else:
            po = PO.objects.create(po=po,description=description)
            po.save()
            messages.success(request, po.po + " is Saved Successfully")
            return redirect('add_po')
    return render (request, 'testApp/add_po.html', locals())

def view_po(request):
    pos = PO.objects.all()
    return render (request, 'testApp/view_po.html', locals())

def edit_po(request,id):
    get_po = PO.objects.get(id=id)
    if request.method == 'POST':
        po = request.POST.get('po')
        description = request.POST.get('description')
        get_po.po=po
        get_po.description=description
        get_po.save()
        messages.success(request, get_po.po + " is updated Successfully")
        return redirect('add_po')
    return render (request, 'testApp/edit_po.html', locals())

# def delete_po(request, id):
#     get_po = PO.objects.get(id=id)
#     get_po.delete()
#     return redirect('add_po')

def add_pso(request):
    psos = PSO.objects.all()
    if request.method == 'POST':
        pso = request.POST.get('pso')
        description = request.POST.get('description')
        if PSO.objects.filter(pso=pso).exists():
            messages.warning(request, pso + " is already entered")
            return redirect('add_pso')
        else:
            pso = PSO.objects.create(pso=pso,description=description)
            pso.save()
            messages.success(request, pso.pso + " is Saved Successfully")
            return redirect('add_pso')
    return render (request, 'testApp/add_pso.html', locals())

def view_pso(request):
    psos = PSO.objects.all()
    return render (request, 'testApp/view_pso.html', locals())

def edit_pso(request,id):
    get_pso = PSO.objects.get(id=id)
    if request.method == 'POST':
        pso = request.POST.get('pso')
        description = request.POST.get('description')
        get_pso.pso=pso
        get_pso.description=description
        get_pso.save()
        messages.success(request, get_pso.pso + " is updated Successfully")
        return redirect('add_pso')
    return render (request, 'testApp/edit_pso.html', locals())

# def delete_pso(request, id):
#     get_pso = PSO.objects.get(id=id)
#     get_pso.delete()
#     return redirect('add_pso')

def attainment_levels(request):
    psos = PSO.objects.all()
    return render (request, 'testApp/attainment_levels.html', locals())

def indirect_attainment(request):
    cos = CO.objects.all()
    indirects = Indirect.objects.all()
    if request.method == 'POST':
        for i in cos:
            print(i.co+"_id")
            co_id = request.POST.get(i.co+"_id")
            co = CO.objects.get(id=co_id)
            if Indirect.objects.filter(co=co).exists():
                messages.warning(request, " Attainment is already entered")
                return redirect('indirect_attainment')
            high = int(request.POST.get(i.co+"_high"))
            medium = int(request.POST.get(i.co+"_medium"))
            low = int(request.POST.get(i.co+"_low"))
            attainment = round((high*3+medium*2+low*1)/178,2)
            print(co, high, medium, low, attainment)
            indirect = Indirect.objects.create(co=co,high=high,medium=medium,low=low,attainment=attainment)
    return render (request, 'testApp/indirect_attainment.html', locals())


def view_indirect_attainment(request):
    indirects = Indirect.objects.all()
    return render (request, 'testApp/view_indirect_attainment.html', locals())

def edit_indirect_attainment(request):
    if request.method == 'POST':
        indirects = Indirect.objects.all()
        for i in indirects:
            indirect_id = request.POST.get("indirect_"+str(i.id))
            high = int(request.POST.get("high_"+str(i.id)))
            medium = int(request.POST.get("medium_"+str(i.id)))
            low = int(request.POST.get("low_"+str(i.id)))
            attainment = round((high*3+medium*2+low*1)/178,2)
            print(indirect_id, high, medium, low, attainment)
            indirect = Indirect.objects.get(id=indirect_id)
            indirect.high=high
            indirect.medium=medium
            indirect.low=low
            indirect.attainment=attainment
            indirect.save()
        messages.success(request, " Successfully Updated the attainment")
    indirects = Indirect.objects.all()
    return render (request, 'testApp/edit_indirect_attainment.html', locals())

def co_po_matrix1(request):
    if CO_PO_Matrix.objects.exists():
        copolevels = CO_PO_Matrix.objects.all()
        if request.method == 'POST':
            for i in copolevels:
                colevel_id = request.POST.get("co"+str(i.id))
                po1 = request.POST.get(str(i.co)+"_po1")
                po2 = request.POST.get(str(i.co)+"_po2")
                po3 = request.POST.get(str(i.co)+"_po3")
                po4 = request.POST.get(str(i.co)+"_po4")
                po5 = request.POST.get(str(i.co)+"_po5")
                po6 = request.POST.get(str(i.co)+"_po6")
                po7 = request.POST.get(str(i.co)+"_po7")
                po8 = request.POST.get(str(i.co)+"_po8")
                po9 = request.POST.get(str(i.co)+"_po9")
                po10 = request.POST.get(str(i.co)+"_po10")
                po11 = request.POST.get(str(i.co)+"_po11")
                po12 = request.POST.get(str(i.co)+"_po12")
                po12 = request.POST.get(str(i.co)+"_po12")
                pso1 = request.POST.get(str(i.co)+"_pso1")
                pso2 = request.POST.get(str(i.co)+"_pso2")
                pso3 = request.POST.get(str(i.co)+"_pso3")
                co= CO_PO_Matrix.objects.get(id=colevel_id)
                co.po1 =po1
                co.po2 =po2
                co.po3 =po3
                co.po4 =po4
                co.po5 =po5
                co.po6 =po6
                co.po7 =po7
                co.po8 =po8
                co.po9 =po9
                co.po10 =po10
                co.po11 =po11
                co.po12 =po12
                co.pso1 =pso1
                co.pso2 =pso2
                co.pso3 =pso3
                co.save()
            messages.success(request, "CO-PO matrix Successfully Updated")
            return redirect('edit_co_po_matrix')
        return render (request, 'testApp/edit_co_po_matrix.html', locals())
    else:
        cos = CO.objects.all()
        if request.method == 'POST':
            for i in cos:
                co_id = request.POST.get("co_id"+str(i.id))
                co = CO.objects.get(id=co_id)
                if CO_PO_Matrix.objects.filter(co=co).exists():
                    messages.warning(request, " CO-PO matrix is already entered")
                    return redirect('co_po_matrix')
                po1 = request.POST.get(i.co+"_po1")
                po2 = request.POST.get(i.co+"_po2")
                po3 = request.POST.get(i.co+"_po3")
                po4 = request.POST.get(i.co+"_po4")
                po5 = request.POST.get(i.co+"_po5")
                po6 = request.POST.get(i.co+"_po6")
                po7 = request.POST.get(i.co+"_po7")
                po8 = request.POST.get(i.co+"_po8")
                po9 = request.POST.get(i.co+"_po9")
                po10 = request.POST.get(i.co+"_po10")
                po11 = request.POST.get(i.co+"_po11")
                po12 = request.POST.get(i.co+"_po12")
                po12 = request.POST.get(i.co+"_po12")
                pso1 = request.POST.get(i.co+"_pso1")
                pso2 = request.POST.get(i.co+"_pso2")
                pso3 = request.POST.get(i.co+"_pso3")
                copolevels = CO_PO_Matrix.objects.create(co=co,po1=po1,po2=po2,po3=po3,po4=po4,po5=po5,po6=po6,
                          po7=po7,po8=po8,po9=po9,po10=po10,po11=po11,po12=po12, pso1=pso1, pso2=pso2,pso3=pso3)
                copolevels.save()
            messages.success(request, " Successfully addd the co-po matrix")
            return redirect('edit_co_po_matrix')
        return render (request, 'testApp/co_po_matrix.html', locals())

def co_po_matrix(request):
    cos = CO.objects.all()
    if request.method == 'POST':
        for i in cos:
            co_id = request.POST.get("co_id"+str(i.id))
            co = CO.objects.get(id=co_id)
            if CO_PO_Matrix.objects.filter(co=co).exists():
                messages.warning(request, " CO-PO matrix is already entered")
                return redirect('co_po_matrix')
            po1 = request.POST.get(i.co+"_po1")
            po2 = request.POST.get(i.co+"_po2")
            po3 = request.POST.get(i.co+"_po3")
            po4 = request.POST.get(i.co+"_po4")
            po5 = request.POST.get(i.co+"_po5")
            po6 = request.POST.get(i.co+"_po6")
            po7 = request.POST.get(i.co+"_po7")
            po8 = request.POST.get(i.co+"_po8")
            po9 = request.POST.get(i.co+"_po9")
            po10 = request.POST.get(i.co+"_po10")
            po11 = request.POST.get(i.co+"_po11")
            po12 = request.POST.get(i.co+"_po12")
            po12 = request.POST.get(i.co+"_po12")
            pso1 = request.POST.get(i.co+"_pso1")
            pso2 = request.POST.get(i.co+"_pso2")
            pso3 = request.POST.get(i.co+"_pso3")
            copolevels = CO_PO_Matrix.objects.create(co=co,po1=po1,po2=po2,po3=po3,po4=po4,po5=po5,po6=po6,
                      po7=po7,po8=po8,po9=po9,po10=po10,po11=po11,po12=po12, pso1=pso1, pso2=pso2,pso3=pso3)
            copolevels.save()
        messages.success(request, " Successfully addd the co-po matrix")
    return render (request, 'testApp/co_po_matrix.html', locals())

def edit_co_po_matrix(request):
    copolevels = CO_PO_Matrix.objects.all()
    if request.method == 'POST':
        for i in copolevels:
            colevel_id = request.POST.get("co"+str(i.id))
            po1 = request.POST.get(str(i.co)+"_po1")
            po2 = request.POST.get(str(i.co)+"_po2")
            po3 = request.POST.get(str(i.co)+"_po3")
            po4 = request.POST.get(str(i.co)+"_po4")
            po5 = request.POST.get(str(i.co)+"_po5")
            po6 = request.POST.get(str(i.co)+"_po6")
            po7 = request.POST.get(str(i.co)+"_po7")
            po8 = request.POST.get(str(i.co)+"_po8")
            po9 = request.POST.get(str(i.co)+"_po9")
            po10 = request.POST.get(str(i.co)+"_po10")
            po11 = request.POST.get(str(i.co)+"_po11")
            po12 = request.POST.get(str(i.co)+"_po12")
            po12 = request.POST.get(str(i.co)+"_po12")
            pso1 = request.POST.get(str(i.co)+"_pso1")
            pso2 = request.POST.get(str(i.co)+"_pso2")
            pso3 = request.POST.get(str(i.co)+"_pso3")
            co= CO_PO_Matrix.objects.get(id=colevel_id)
            co.po1 =po1
            co.po2 =po2
            co.po3 =po3
            co.po4 =po4
            co.po5 =po5
            co.po6 =po6
            co.po7 =po7
            co.po8 =po8
            co.po9 =po9
            co.po10 =po10
            co.po11 =po11
            co.po12 =po12
            co.pso1 =pso1
            co.pso2 =pso2
            co.pso3 =pso3
            co.save()
        messages.success(request, "CO-PO matrix Successfully Updated")
        return redirect('edit_co_po_matrix')
    return render (request, 'testApp/edit_co_po_matrix.html', locals())


def view_co_po_matrix(request):
    copolevels = CO_PO_Matrix.objects.all()
    # po1_avg = CO_PO_Matrix.objects.aggregate(Sum('po1'))['po1__sum'] / CO_PO_Matrix.objects.filter(po1__in=[1,2,3]).count()
    po1_avg = CO_PO_Matrix.objects.filter(po1__gt=0).aggregate(Avg('po1'))['po1__avg']
    po2_avg = CO_PO_Matrix.objects.filter(po2__gt=0).aggregate(Avg('po2'))['po2__avg']
    po3_avg = CO_PO_Matrix.objects.filter(po3__gt=0).aggregate(Avg('po3'))['po3__avg']
    po4_avg = CO_PO_Matrix.objects.filter(po4__gt=0).aggregate(Avg('po4'))['po4__avg']
    po5_avg = CO_PO_Matrix.objects.filter(po5__gt=0).aggregate(Avg('po5'))['po5__avg']
    po6_avg = CO_PO_Matrix.objects.filter(po6__gt=0).aggregate(Avg('po6'))['po6__avg']
    po7_avg = CO_PO_Matrix.objects.filter(po7__gt=0).aggregate(Avg('po7'))['po7__avg']
    po8_avg = CO_PO_Matrix.objects.filter(po8__gt=0).aggregate(Avg('po8'))['po8__avg']
    po9_avg = CO_PO_Matrix.objects.filter(po9__gt=0).aggregate(Avg('po9'))['po9__avg']
    po10_avg = CO_PO_Matrix.objects.filter(po10__gt=0).aggregate(Avg('po10'))['po10__avg']
    po11_avg = CO_PO_Matrix.objects.filter(po11__gt=0).aggregate(Avg('po11'))['po11__avg']
    po12_avg = CO_PO_Matrix.objects.filter(po12__gt=0).aggregate(Avg('po12'))['po12__avg']

    pso1_avg = CO_PO_Matrix.objects.filter(pso1__gt=0).aggregate(Avg('pso1'))['pso1__avg']
    pso2_avg = CO_PO_Matrix.objects.filter(pso2__gt=0).aggregate(Avg('pso2'))['pso2__avg']
    pso3_avg = CO_PO_Matrix.objects.filter(pso3__gt=0).aggregate(Avg('pso3'))['pso3__avg']
    return render (request, 'testApp/view_co_po_matrix.html', locals())

def course_attainment(request):

    cos = CO.objects.all()
    for co in cos:
        internal = Intenal_Question.objects.filter(co_mapped=co).aggregate(Avg('attainment_level'))['attainment_level__avg']
        external = External_Question.objects.filter(co_mapped=co).aggregate(Avg('attainment_level'))['attainment_level__avg']
        direct = internal*0.3 + external*0.7

        indirect = Indirect.objects.get(co=co)

        if  not Course_Attainment.objects.filter(co=co).exists():
            final = (direct*0.8) + (indirect.attainment*0.2)
            co_attainment = Course_Attainment.objects.create(co=co,internal=internal,external=external,direct=direct,indirect=indirect,final=final)
            co.save()
    course_attainment_value = Course_Attainment.objects.all().aggregate(Avg('final'))['final__avg']

    course_attainment = Course_Attainment.objects.all()
    return render (request, 'testApp/course_attainment.html', locals())

def po_attainment(request):

    po1_avg = CO_PO_Matrix.objects.filter(po1__gt=0).aggregate(Avg('po1'))['po1__avg']
    po2_avg = CO_PO_Matrix.objects.filter(po2__gt=0).aggregate(Avg('po2'))['po2__avg']
    po3_avg = CO_PO_Matrix.objects.filter(po3__gt=0).aggregate(Avg('po3'))['po3__avg']
    po4_avg = CO_PO_Matrix.objects.filter(po4__gt=0).aggregate(Avg('po4'))['po4__avg']
    po5_avg = CO_PO_Matrix.objects.filter(po5__gt=0).aggregate(Avg('po5'))['po5__avg']
    po6_avg = CO_PO_Matrix.objects.filter(po6__gt=0).aggregate(Avg('po6'))['po6__avg']
    po7_avg = CO_PO_Matrix.objects.filter(po7__gt=0).aggregate(Avg('po7'))['po7__avg']
    po8_avg = CO_PO_Matrix.objects.filter(po8__gt=0).aggregate(Avg('po8'))['po8__avg']
    po9_avg = CO_PO_Matrix.objects.filter(po9__gt=0).aggregate(Avg('po9'))['po9__avg']
    po10_avg = CO_PO_Matrix.objects.filter(po10__gt=0).aggregate(Avg('po10'))['po10__avg']
    po11_avg = CO_PO_Matrix.objects.filter(po11__gt=0).aggregate(Avg('po11'))['po11__avg']
    po12_avg = CO_PO_Matrix.objects.filter(po12__gt=0).aggregate(Avg('po12'))['po12__avg']

    pso1_avg = CO_PO_Matrix.objects.filter(pso1__gt=0).aggregate(Avg('pso1'))['pso1__avg']
    pso2_avg = CO_PO_Matrix.objects.filter(pso2__gt=0).aggregate(Avg('pso2'))['pso2__avg']
    pso3_avg = CO_PO_Matrix.objects.filter(pso3__gt=0).aggregate(Avg('pso3'))['pso3__avg']

    course_attainment= Course_Attainment.objects.all().aggregate(Avg('final'))['final__avg']


    po1_attainment = (po1_avg*course_attainment)/3 if po1_avg is not None else None
    po2_attainment = (po2_avg*course_attainment)/3 if po2_avg is not None else None
    po3_attainment = (po3_avg*course_attainment)/3 if po3_avg is not None else None
    po4_attainment = (po4_avg*course_attainment)/3 if po4_avg is not None else None
    po5_attainment = (po5_avg*course_attainment)/3 if po5_avg is not None else None
    po6_attainment = (po6_avg*course_attainment)/3 if po6_avg is not None else None
    po7_attainment = (po7_avg*course_attainment)/3 if po7_avg is not None else None
    po8_attainment = (po8_avg*course_attainment)/3 if po8_avg is not None else None
    po9_attainment = (po9_avg*course_attainment)/3 if po9_avg is not None else None
    po10_attainment = (po10_avg*course_attainment)/3 if po10_avg is not None else None
    po11_attainment = (po11_avg*course_attainment)/3 if po11_avg is not None else None
    po12_attainment = (po12_avg*course_attainment)/3 if po12_avg is not None else None
    pso1_attainment = (pso1_avg*course_attainment)/3 if pso1_avg is not None else None
    pso2_attainment = (pso2_avg*course_attainment)/3 if pso2_avg is not None else None
    pso3_attainment = (pso3_avg*course_attainment)/3 if pso3_avg is not None else None

    # saving to database
    PO_Attainment.objects.all().delete()
    PSO_Attainment.objects.all().delete()
    po1 = PO.objects.get(id=13)
    PO_Attainment.objects.create(po=po1, attainment=po1_attainment)
    po2 = PO.objects.get(id=14)
    PO_Attainment.objects.create(po=po2, attainment=po2_attainment)
    po3 = PO.objects.get(id=15)
    PO_Attainment.objects.create(po=po3, attainment=po3_attainment)
    po4 = PO.objects.get(id=16)
    PO_Attainment.objects.create(po=po4, attainment=po4_attainment)
    po5 = PO.objects.get(id=17)
    PO_Attainment.objects.create(po=po5, attainment=po5_attainment)
    po6 = PO.objects.get(id=18)
    PO_Attainment.objects.create(po=po6, attainment=po6_attainment)
    po7 = PO.objects.get(id=19)
    PO_Attainment.objects.create(po=po7, attainment=po7_attainment)
    po8 = PO.objects.get(id=20)
    PO_Attainment.objects.create(po=po8, attainment=po8_attainment)
    po9 = PO.objects.get(id=21)
    PO_Attainment.objects.create(po=po9, attainment=po9_attainment)
    po10 = PO.objects.get(id=22)
    PO_Attainment.objects.create(po=po10, attainment=po10_attainment)
    po11 = PO.objects.get(id=23)
    PO_Attainment.objects.create(po=po11, attainment=po11_attainment)
    po12 = PO.objects.get(id=24)
    PO_Attainment.objects.create(po=po12, attainment=po12_attainment)
    print(PSO.objects.all().values())
    pso1 = PSO.objects.get(id=1)
    PSO_Attainment.objects.create(pso=pso1, attainment=pso1_attainment)
    pso2 = PSO.objects.get(id=2)
    PSO_Attainment.objects.create(pso=pso2, attainment=pso2_attainment)
    pso3 = PSO.objects.get(id=3)
    PSO_Attainment.objects.create(pso=pso3, attainment=pso3_attainment)

    return render (request, 'testApp/po_attainment.html', locals())




























def home(request):
    cos = CO.objects.all()
    pos = PO.objects.all()
    psos = PSO.objects.all()
    indirects = Indirect.objects.all()
    copomaps = CO_PO_mapping.objects.all()
    copolevels =CO_PO_Matrix.objects.all()
    # copsolevels =CO_PSO_Matrix.objects.all()


    from django.db.models import Avg, Sum,Count
    # po1_avg = CO_PO_Matrix.objects.aggregate(Sum('po1'))['po1__sum'] / CO_PO_Matrix.objects.filter(po1__in=[1,2,3]).count()
    po1_avg = CO_PO_Matrix.objects.filter(po1__gt=0).aggregate(Avg('po1'))['po1__avg']
    po2_avg = CO_PO_Matrix.objects.filter(po2__gt=0).aggregate(Avg('po2'))['po2__avg']
    po3_avg = CO_PO_Matrix.objects.filter(po3__gt=0).aggregate(Avg('po3'))['po3__avg']
    po4_avg = CO_PO_Matrix.objects.filter(po4__gt=0).aggregate(Avg('po4'))['po4__avg']
    po5_avg = CO_PO_Matrix.objects.filter(po5__gt=0).aggregate(Avg('po5'))['po5__avg']
    po6_avg = CO_PO_Matrix.objects.filter(po6__gt=0).aggregate(Avg('po6'))['po6__avg']
    po7_avg = CO_PO_Matrix.objects.filter(po7__gt=0).aggregate(Avg('po7'))['po7__avg']
    po8_avg = CO_PO_Matrix.objects.filter(po8__gt=0).aggregate(Avg('po8'))['po8__avg']
    po9_avg = CO_PO_Matrix.objects.filter(po9__gt=0).aggregate(Avg('po9'))['po9__avg']
    po10_avg = CO_PO_Matrix.objects.filter(po10__gt=0).aggregate(Avg('po10'))['po10__avg']
    po11_avg = CO_PO_Matrix.objects.filter(po11__gt=0).aggregate(Avg('po11'))['po11__avg']
    po12_avg = CO_PO_Matrix.objects.filter(po12__gt=0).aggregate(Avg('po12'))['po12__avg']

    pso1_avg = CO_PO_Matrix.objects.filter(pso1__gt=0).aggregate(Avg('pso1'))['pso1__avg']
    pso2_avg = CO_PO_Matrix.objects.filter(pso2__gt=0).aggregate(Avg('pso2'))['pso2__avg']
    pso3_avg = CO_PO_Matrix.objects.filter(pso3__gt=0).aggregate(Avg('pso3'))['pso3__avg']


    return render(request, 'testApp/home.html',locals())




def home1(request):
    # Question.objects.all().delete()
    # Mid1.objects.all().delete()
    # Mid2.objects.all().delete()
    # import csv
    # with open('test1.csv', 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     next(csv_reader)
    #     next(csv_reader)
    #     next(csv_reader)
    #     lines = []
    #     for index, line in enumerate(csv_reader,1):
    #         # iterate through each element and replace empty strings with None
    #         for i in range(len(line)):
    #             if line[i] == '':
    #                 line[i] = None
    #         lines.append(line)
    #     print(lines[0])
    #     for g, student in enumerate(Student.objects.all(),0):
    #         i=1
    #         for q in QP_mid1.objects.all():
    #             marks = lines[g][i]
    #             print("Marks = ",student, q, marks)
    #             m1marks = Mid1(student=student,question=q,marks=marks)
    #             m1marks.save()
    #             i=i+1
    #     for g, student in enumerate(Student.objects.all(),0):
    #         i=7
    #         for q in QP_mid2.objects.all():
    #             marks = lines[g][i]
    #             print("Marks = ",student, q, marks)
    #             m2marks = Mid2(student=student,question=q,marks=marks)
    #             m2marks.save()
    #             i=i+1
    #     for g, student in enumerate(Student.objects.all(),0):
    #         marks = lines[g][13]
    #         print("Marks = ",student, marks)
    #         seemarks = SEE(student=student, marks=marks)
    #         seemarks.save()
    #         i=i+1



    # StudentMark.objects.all().delete()
    # import csv
    # with open('test1.csv', 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     next(csv_reader)
    #     next(csv_reader)
    #     next(csv_reader)
    #     for line in csv_reader:
    #         print(line)
    #         lst = ['Geeks', '', 'CS', '', '']
    #         # iterate through each element and replace empty strings with None
    #         for i in range(len(line)):
    #             if line[i] == '':
    #                 line[i] = None
    #         print(line)
    #         student = StudentMark (rollno=line[0],
    #                                m1_q1_marks=line[1],
    #                                m1_q2_marks=line[2],
    #                                m1_q3_marks=line[3],
    #                                m1_q4_marks=line[4],
    #                                m1_objective_marks=line[5],
    #                                m1_assignment_marks=line[6],
    #                                m2_q1_marks=line[7],
    #                                m2_q2_marks=line[8],
    #                                m2_q3_marks=line[9],
    #                                m2_q4_marks=line[10],
    #                                m2_objective_marks=line[11],
    #                                m2_assignment_marks=line[12],
    #                                ext_marks=line[13])
    #         student.save()
    studentsmarks = StudentMark.objects.all()

    m1_q1_attempt_count = StudentMark.objects.filter(m1_q1_marks__gte=0).count()
    m1_q2_attempt_count = StudentMark.objects.filter(m1_q2_marks__gte=0).count()
    m1_q3_attempt_count = StudentMark.objects.filter(m1_q3_marks__gte=0).count()
    m1_q4_attempt_count = StudentMark.objects.filter(m1_q4_marks__gte=0).count()
    m1_quiz_attempt_count = StudentMark.objects.filter(m1_objective_marks__gte=0).count()
    m1_assign_attempt_count = StudentMark.objects.filter(m1_assignment_marks__gte=0).count()
    m2_q1_attempt_count = StudentMark.objects.filter(m2_q1_marks__gte=0).count()
    m2_q2_attempt_count = StudentMark.objects.filter(m2_q2_marks__gte=0).count()
    m2_q3_attempt_count = StudentMark.objects.filter(m2_q3_marks__gte=0).count()
    m2_q4_attempt_count = StudentMark.objects.filter(m2_q4_marks__gte=0).count()
    m2_quiz_attempt_count = StudentMark.objects.filter(m2_objective_marks__gte=0).count()
    m2_assign_attempt_count = StudentMark.objects.filter(m2_assignment_marks__gte=0).count()
    ext_attempt_count = StudentMark.objects.filter(ext_marks__gte=0).count()


    m1_q1_gth_count = StudentMark.objects.filter(m1_q1_marks__gte=0.6*5).count()
    m1_q2_gth_count = StudentMark.objects.filter(m1_q2_marks__gte=0.6*5).count()
    m1_q3_gth_count = StudentMark.objects.filter(m1_q3_marks__gte=0.6*5).count()
    m1_q4_gth_count = StudentMark.objects.filter(m1_q4_marks__gte=0.6*5).count()
    m1_quiz_gth_count = StudentMark.objects.filter(m1_objective_marks__gte=0.6*10).count()
    m1_assign_gth_count = StudentMark.objects.filter(m1_assignment_marks__gte=0.6*5).count()
    m2_q1_gth_count = StudentMark.objects.filter(m2_q1_marks__gte=0.6*5).count()
    m2_q2_gth_count = StudentMark.objects.filter(m2_q2_marks__gte=0.6*5).count()
    m2_q3_gth_count = StudentMark.objects.filter(m2_q3_marks__gte=0.6*5).count()
    m2_q4_gth_count = StudentMark.objects.filter(m2_q4_marks__gte=0.6*5).count()
    m2_quiz_gth_count = StudentMark.objects.filter(m2_objective_marks__gte=0.6*10).count()
    m2_assign_gth_count = StudentMark.objects.filter(m2_assignment_marks__gte=0.6*5).count()
    ext_gth_count = StudentMark.objects.filter(ext_marks__gte=0.4*75).count()
    import math
    m1_q1_gth_percnt = round((m1_q1_gth_count/m1_q1_attempt_count)*100)
    m1_q2_gth_percnt = round((m1_q2_gth_count/m1_q2_attempt_count)*100)
    m1_q3_gth_percnt = round((m1_q3_gth_count/m1_q3_attempt_count)*100)
    m1_q4_gth_percnt = round((m1_q4_gth_count/m1_q4_attempt_count)*100)
    m1_quiz_gth_percnt = round((m1_quiz_gth_count/m1_quiz_attempt_count)*100)
    m1_assign_gth_percnt = round((m1_assign_gth_count/m1_assign_attempt_count)*100)
    m2_q1_gth_percnt = round((m2_q1_gth_count/m2_q1_attempt_count)*100)
    m2_q2_gth_percnt = round((m2_q2_gth_count/m2_q2_attempt_count)*100)
    m2_q3_gth_percnt = round((m2_q3_gth_count/m2_q3_attempt_count)*100)
    m2_q4_gth_percnt = round((m2_q4_gth_count/m2_q4_attempt_count)*100)
    m2_quiz_gth_percnt = round((m2_quiz_gth_count/m2_quiz_attempt_count)*100)
    m2_assign_gth_percnt = round((m2_assign_gth_count/m2_assign_attempt_count)*100)
    ext_gth_percnt = round((ext_gth_count/ext_attempt_count)*100)

    # attainment levels
    for i in Intenal_Question.objects.all():
        if i.id==1:
            attempt_count = StudentMark.objects.filter(m1_q1_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m1_q1_marks__gte=0.6*5).count()
        elif i.id==2:
            attempt_count = StudentMark.objects.filter(m1_q2_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m1_q2_marks__gte=0.6*5).count()
        elif i.id==3:
            attempt_count = StudentMark.objects.filter(m1_q3_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m1_q3_marks__gte=0.6*5).count()
        elif i.id==4:
            attempt_count = StudentMark.objects.filter(m1_q4_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m1_q4_marks__gte=0.6*5).count()
        elif i.id==5:
            attempt_count = StudentMark.objects.filter(m1_objective_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m1_objective_marks__gte=0.6*10).count()
        elif i.id==6:
            attempt_count = StudentMark.objects.filter(m1_assignment_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m1_assignment_marks__gte=0.6*5).count()

        if i.id==7:
            attempt_count = StudentMark.objects.filter(m2_q1_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m2_q1_marks__gte=0.6*5).count()
        elif i.id==8:
            attempt_count = StudentMark.objects.filter(m2_q2_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m2_q2_marks__gte=0.6*5).count()
        elif i.id==9:
            attempt_count = StudentMark.objects.filter(m2_q3_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m2_q3_marks__gte=0.6*5).count()
        elif i.id==10:
            attempt_count = StudentMark.objects.filter(m2_q4_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m2_q4_marks__gte=0.6*5).count()
        elif i.id==11:
            attempt_count = StudentMark.objects.filter(m2_objective_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m2_objective_marks__gte=0.6*10).count()
        elif i.id==12:
            attempt_count = StudentMark.objects.filter(m2_assignment_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(m2_assignment_marks__gte=0.6*5).count()
        # elif i.id==26:
        #     attempt_count = StudentMark.objects.filter(ext_marks__gte=0).count()
        #     gth_count = StudentMark.objects.filter(ext_marks__gte=0.4*75).count()
        gth_percnt = round((gth_count/attempt_count)*100)
        if gth_percnt >=76:
            i.attainment_level = 3
            i.save()
        elif gth_percnt >=61:
            i.attainment_level = 2
            i.save()
        elif gth_percnt >=51:
            i.attainment_level = 1
            i.save()
        else:
            i.attainment_level = 0
            i.save()

    for i in External_Question.objects.all():
        if i.id==27:
            attempt_count = StudentMark.objects.filter(ext_marks__gte=0).count()
            gth_count = StudentMark.objects.filter(ext_marks__gte=0.4*75).count()
        gth_percnt = round((gth_count/attempt_count)*100)
        if gth_percnt >=76:
            i.attainment_level = 3
            i.save()
        elif gth_percnt >=61:
            i.attainment_level = 2
            i.save()
        elif gth_percnt >=51:
            i.attainment_level = 1
            i.save()
        else:
            i.attainment_level = 0
            i.save()

    indirects = Indirect.objects.all()
    copolevels =CO_PO_Matrix.objects.all()
    from django.db.models import Avg, Sum,Count
    po1_avg = CO_PO_Matrix.objects.filter(po1__gt=0).aggregate(Avg('po1'))['po1__avg']
    po2_avg = CO_PO_Matrix.objects.filter(po2__gt=0).aggregate(Avg('po2'))['po2__avg']
    po3_avg = CO_PO_Matrix.objects.filter(po3__gt=0).aggregate(Avg('po3'))['po3__avg']
    po4_avg = CO_PO_Matrix.objects.filter(po4__gt=0).aggregate(Avg('po4'))['po4__avg']
    po5_avg = CO_PO_Matrix.objects.filter(po5__gt=0).aggregate(Avg('po5'))['po5__avg']
    po6_avg = CO_PO_Matrix.objects.filter(po6__gt=0).aggregate(Avg('po6'))['po6__avg']
    po7_avg = CO_PO_Matrix.objects.filter(po7__gt=0).aggregate(Avg('po7'))['po7__avg']
    po8_avg = CO_PO_Matrix.objects.filter(po8__gt=0).aggregate(Avg('po8'))['po8__avg']
    po9_avg = CO_PO_Matrix.objects.filter(po9__gt=0).aggregate(Avg('po9'))['po9__avg']
    po10_avg = CO_PO_Matrix.objects.filter(po10__gt=0).aggregate(Avg('po10'))['po10__avg']
    po11_avg = CO_PO_Matrix.objects.filter(po11__gt=0).aggregate(Avg('po11'))['po11__avg']
    po12_avg = CO_PO_Matrix.objects.filter(po12__gt=0).aggregate(Avg('po12'))['po12__avg']
    pso1_avg = CO_PO_Matrix.objects.filter(pso1__gt=0).aggregate(Avg('pso1'))['pso1__avg']
    pso2_avg = CO_PO_Matrix.objects.filter(pso2__gt=0).aggregate(Avg('pso2'))['pso2__avg']
    pso3_avg = CO_PO_Matrix.objects.filter(pso3__gt=0).aggregate(Avg('pso3'))['pso3__avg']

    intenal_questions  = Intenal_Question.objects.all()
    external_questions = External_Question.objects.all()
    course_attainment = Course_Attainment.objects.all()
    course_attainment_value = Course_Attainment.objects.all().aggregate(Avg('final'))['final__avg']

    po1_attainment = (po1_avg*course_attainment_value)/3 if po1_avg is not None else None
    po2_attainment = (po2_avg*course_attainment_value)/3 if po2_avg is not None else None
    po3_attainment = (po3_avg*course_attainment_value)/3 if po3_avg is not None else None
    po4_attainment = (po4_avg*course_attainment_value)/3 if po4_avg is not None else None
    po5_attainment = (po5_avg*course_attainment_value)/3 if po5_avg is not None else None
    po6_attainment = (po6_avg*course_attainment_value)/3 if po6_avg is not None else None
    po7_attainment = (po7_avg*course_attainment_value)/3 if po7_avg is not None else None
    po8_attainment = (po8_avg*course_attainment_value)/3 if po8_avg is not None else None
    po9_attainment = (po9_avg*course_attainment_value)/3 if po9_avg is not None else None
    po10_attainment = (po10_avg*course_attainment_value)/3 if po10_avg is not None else None
    po11_at8ainment = (po11_avg*course_attainment_value)/3 if po11_avg is not None else None
    po12_attainment = (po12_avg*course_attainment_value)/3 if po12_avg is not None else None
    pso1_attainment = (pso1_avg*course_attainment_value)/3 if pso1_avg is not None else None
    pso2_attainment = (pso2_avg*course_attainment_value)/3 if pso2_avg is not None else None
    pso3_a3tainment = (pso3_avg*course_attainment_value)/3 if pso3_avg is not None else None


    #for Graph
    co1 = Course_Attainment.objects.get(co=9)
    co1_attained_value = co1.final
    co2 = Course_Attainment.objects.get(co=10)
    co2_attained_value = co2.final
    co3 = Course_Attainment.objects.get(co=11)
    co3_attained_value = co3.final
    co4 = Course_Attainment.objects.get(co=12)
    co4_attained_value = co4.final
    co5 = Course_Attainment.objects.get(co=13)
    co5_attained_value = co5.final
    print(co1_attained_value,co2_attained_value,co3_attained_value,co4_attained_value,co5_attained_value)
    return render (request, 'testApp/home1.html', locals())

def home2(request):
    students = Student.objects.all()
    for student in students:
        m = Mid1.objects.filter(student=student)
        for i in m:
            print(i.student.rollno, i.question.question, i.marks)
    return render (request, 'testApp/home2.html', locals())

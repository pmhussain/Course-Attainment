"""
URL configuration for csvread_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home1', views.home1, name='home1'),
    path('home2', views.home2, name='home2'),
    path('add_co', views.add_co, name='add_co'),
    path('view_co', views.view_co, name='view_co'),
    path('edit_co/<int:id>', views.edit_co, name='edit_co'),
    path('delete_co/<int:id>', views.delete_co, name='delete_co'),

    path('add_po', views.add_po, name='add_po'),
    path('view_po', views.view_po, name='view_po'),
    path('edit_po/<int:id>', views.edit_po, name='edit_po'),
    # path('delete_po/<int:id>', views.delete_po, name='delete_po'),

    path('add_pso', views.add_pso, name='add_pso'),
    path('view_pso', views.view_pso, name='view_pso'),
    path('edit_pso/<int:id>', views.edit_pso, name='edit_pso'),
    # path('delete_pso/<int:id>', views.delete_pso, name='delete_pso'),

    path('attainment_levels', views.attainment_levels, name='attainment_levels'),
    path('indirect_attainment', views.indirect_attainment, name='indirect_attainment'),
    path('view_indirect_attainment', views.view_indirect_attainment, name='view_indirect_attainment'),
    path('edit_indirect_attainment', views.edit_indirect_attainment, name='edit_indirect_attainment'),

    path('co_po_matrix', views.co_po_matrix, name='co_po_matrix'),
    path('co_po_matrix1', views.co_po_matrix1, name='co_po_matrix1'),#add or update in same link
    path('edit_co_po_matrix', views.edit_co_po_matrix, name='edit_co_po_matrix'),
    path('view_co_po_matrix', views.view_co_po_matrix, name='view_co_po_matrix'),

    path('course_attainment', views.course_attainment, name='course_attainment'),
    path('po_attainment', views.po_attainment, name='po_attainment'),
]

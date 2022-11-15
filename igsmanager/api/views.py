from django.shortcuts import render
from rest_framework import generics
from django.views.generic.base import TemplateView
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
import requests
class EmployeeCreateAndListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.order_by('id').select_related('department')


class DepartmentCreateAndListView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.order_by('id')   


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.order_by('id').select_related('department')
    group_name = 'employee_detail'


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.order_by('id')
    group_name = 'department_detail'

class EmployeeTableView(TemplateView):
    template_name = 'index.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super(EmployeeTableView, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()

        return context
        
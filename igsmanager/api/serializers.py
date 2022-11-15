from rest_framework import serializers
from .models import Employee, Department
from rest_framework.fields import empty
from django.http import QueryDict

class EmployeeSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, data=empty, **kwargs):
        if (data is not empty) and (not isinstance(data, QueryDict)) and (isinstance(data.get('department'), str)):
            department = Department.objects.filter(name__iexact=data['department']).first()
            data['department'] = department.id if department is not None else 0
        return super().__init__(instance, data, **kwargs)
    
    def to_representation(self, instance: Employee):
        representation = super(EmployeeSerializer, self).to_representation(instance)
        representation['department'] = instance.department.name
        return representation
    
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name')
from django.urls import path
from .views import EmployeeCreateAndListView , DepartmentCreateAndListView
from .views import EmployeeDetailView, DepartmentDetailView, EmployeeTableView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='IGS Employee Manager API')

urlpatterns = [
    path('', EmployeeTableView.as_view()),
    path('doc', schema_view),
    
    path('employee/', EmployeeCreateAndListView.as_view()),
    
    path('department/', DepartmentCreateAndListView.as_view()),
    
    path('employee/<int:pk>/', EmployeeDetailView.as_view()),
    
    path('department/<int:pk>/', DepartmentDetailView.as_view()),
]
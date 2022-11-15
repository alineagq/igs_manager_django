from django.urls import path
from .views import EmployeeCreateAndListView , DepartmentCreateAndListView
from .views import EmployeeDetailView, DepartmentDetailView, EmployeeTableView


urlpatterns = [
    path('', EmployeeTableView.as_view()),
    
    path('employee/', EmployeeCreateAndListView.as_view()),
    path('employee', EmployeeCreateAndListView.as_view()),
    
    path('department/', DepartmentCreateAndListView.as_view()),
    path('department', DepartmentCreateAndListView.as_view()),
    
    path('employee/<int:pk>/', EmployeeDetailView.as_view()),
    path('employee/<int:pk>', EmployeeDetailView.as_view()),
    
    path('department/<int:pk>/', DepartmentDetailView.as_view()),
    path('department/<int:pk>', DepartmentDetailView.as_view()),
]
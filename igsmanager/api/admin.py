from django.contrib import admin
from .models import Employee, Department


admin.site.empty_value_display = 'NULL'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    list_filter = ('name', 'email', 'department')
    list_display_links = 'name',
    list_per_page = 50
    list_select_related = False
    ordering = 'name',
    search_fields = ('name', 'email', 'department')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = 'name',
    list_per_page = 50
    list_select_related = False
    ordering = 'name',
    search_fields = '^name',
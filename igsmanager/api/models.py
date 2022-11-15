from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')

    def __str__(self):
        return "%s %s" % (self.name, self.department)

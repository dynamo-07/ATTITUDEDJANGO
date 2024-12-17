from django.db import models

# Create your models here.
class Employee_Data(models.Model):
    full_name = models.CharField(primary_key = True,max_length=100)  
    email = models.EmailField()        
    phone = models.CharField(max_length=15)       
    department = models.CharField(max_length=50)  
    joining_date = models.DateField()             

    def __str__(self):
        return self.full_name

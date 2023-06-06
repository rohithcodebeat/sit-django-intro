from django.db import models

# Create your models here.
# model is meant by a table 
"""
Name -> char
Rollno -> Int
Dob -> DateField
Branch -> char
year_of_joining -> DateField
"""
class StudentDetailModel(models.Model):
    name          =  models.CharField(max_length=100)
    roll_no       =  models.IntegerField(unique=True)
    date_of_birth =  models.DateField()
    branch        =  models.CharField(max_length=100)
    year_of_joining = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    









from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    student_number = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Student: {self.first_name}{self.last_name}'
    

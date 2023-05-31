from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        return f'{self.first_name}'

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    student = models.ManyToManyField(Student,related_name='Students')

    def __str__(self) -> str:
        return f'{self.name}'
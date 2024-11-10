from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.IntegerField(max_length=20)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name

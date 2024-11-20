from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=20)
    # registration = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=20)
    duration = models.IntegerField()
    course_id = models.CharField(max_length=20)
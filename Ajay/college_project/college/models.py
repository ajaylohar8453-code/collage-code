from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.first_name
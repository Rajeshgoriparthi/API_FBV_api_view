from django.db import models

# Create your models here.


class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    age=models.CharField(max_length=2)


    def __str__(self):
        return self.ename
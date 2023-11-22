from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=100)
    fam = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    tg_id = models.IntegerField(unique=True)
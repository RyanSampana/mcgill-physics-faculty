from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=200,default="www.physics.mcgill.ca")
    phone = models.CharField(max_length=100,default="+1 514 398 phone")
    office = models.CharField(max_length=100,default="RHB")
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name


#class Professor(models.Model):
#    name = models.CharField(max_length=40)
#    email = models.CharField(max_length=100)
#    website = models.CharField(max_length=100)
#    office = models.CharField(max_length=100)
#    phone = models.CharField(max_length=100)
#    title = models.CharField(max_length=100)
#    image = models.CharField(max_length=200)
#    
#    def __str__(self):
#        return self.name
#    
#class Interest(models.Model):
#    interest = models.CharField(max_length=100)
#    professor = models.ManyToManyField(Professor)
#    
#    def __str__(self):
#        return self.interest
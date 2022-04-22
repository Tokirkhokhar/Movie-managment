from audioop import maxpp
from curses import meta
from distutils.command.upload import upload
from email.policy import default

from pyexpat import model
from turtle import title
from django.db import models

class Movielist(models.Model):

    Id = models.AutoField(primary_key=True)
    imgae=models.ImageField(upload_to ='static/Images',default=" ")
    title = models.CharField(max_length=70)
    desc = models.CharField(max_length=300)
    rDate = models.DateField()
   
    vote = models.IntegerField()

    def __str__(self) :
        return (self.title)

class Actorlist(models.Model):
  
     Id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=70)
     birthdate = models.DateField()
     def __str__(self) :
        return (self.name)

class Role(models.Model):
    r_id= models.AutoField
    a_id = models.ForeignKey('Actorlist',on_delete=models.CASCADE)
    m_id = models.ForeignKey('Movielist',on_delete=models.CASCADE)


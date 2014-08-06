from django.db import models

# Create your models here.
class Gendar(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
      return self.name

class Busyo(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
      return self.name

class Meibo(models.Model):
    name = models.CharField(max_length=200)
    gendar = models.ForeignKey(Gendar)
    busyo = models.ForeignKey(Busyo)
    dob = models.DateField('day of birth')
    def __unicode__(self):
      return self.name


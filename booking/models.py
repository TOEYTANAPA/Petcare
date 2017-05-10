from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Car1(models.Model):	
	"""docstring for Event"""
	day=models.CharField(max_length=10,blank=False,null=False,default="")
	time=models.CharField(max_length=10,blank=False,null=False,default="")


class Car2(models.Model):	
	"""docstring for Event"""
	day=models.CharField(max_length=10,blank=False,null=False,default="")
	time=models.CharField(max_length=10,blank=False,null=False,default="")

class Booking(models.Model):
	user=models.CharField(max_length=10,blank=False,null=False,default="")
	dog=models.TextField(max_length=10,blank=False,null=False,default="")
	total=models.FloatField(max_length=10,blank=False,null=False,default="")
	service=models.TextField(max_length=100,blank=False,null=False,default="")
	location=models.CharField(max_length=1000,blank=False,null=False,default="")
	day=models.CharField(max_length=10,blank=False,null=False,default="")
	time=models.CharField(max_length=10,blank=False,null=False,default="")

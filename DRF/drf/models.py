from django.db import models

class Company(models.Model):
	name=models.CharField(max_length=50)
	location=models.CharField(max_length=100)
	about=models.TextField()
	type=models.CharField(max_length=10)



class Employee(models.Model):
	name=models.CharField(max_length=20)
	department=models.CharField(max_length=10)
	
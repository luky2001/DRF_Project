from django.db import models

class Company(models.Model):
	name=models.CharField(max_length=50)
	location=models.CharField(max_length=100)
	about=models.TextField()
	type=models.CharField(max_length=10)
	



from django.db import models

class internshiptype(models.Model):
	interntype=models.CharField(max_length=100)
	def __unicode__(self):
		return self.interntype

class internshipin(models.Model):
	internarea=models.CharField(max_length=150)
	def __unicode__(self):
		return self.internarea

class internships(models.Model):
	companyname=models.CharField(max_length=150)
	internarea=models.ForeignKey(internshipin)
	interntype=models.ForeignKey(internshiptype)
	postd=models.DateField()
	lastd=models.DateField()
	Estartd=models.DateField()
	timeperiod=models.IntegerField()
	abotcom=models.TextField()
	abotintern=models.TextField()
	

class Sex(models.Model):
	sex=models.CharField(max_length=10)
	def __unicode__(self):
		return self.sex

class pi(models.Model):
	name=models.CharField(max_length=100)
	sex=models.ForeignKey(Sex)
	dob=models.DateField()
	email=models.EmailField()
	password=models.CharField(max_length=100)
	def __unicode__(self):
		return self.email
	
	

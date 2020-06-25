from django.db import models
from django.contrib.auth.models import User

class Trial_Class(models.Model):
	user_name = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
	date = models.CharField(max_length=200, null=True)
	time = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.user_name.username

class Assign_Classes(models.Model):
	CLASS_CHOICE=(
			("Maths","Maths"),
			("English","English"),
			("Hindi","Hindi"),
		)	
	user_name = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
	class_name= models.CharField(max_length=200, null=True,choices = CLASS_CHOICE)
	on_date = models.DateTimeField()

	def __str__(self):
		return self.user_name.username

class Assign_Questions(models.Model):
	CLASS_CHOICE=(
			("What is the sum of first two prime numbers?","Maths_Question"),
			("What is a noun? ", "English_Question"),
			("संज्ञा क्या है?","Hindi_Question"),
		)	
	user_name = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE)
	which_question= models.CharField(max_length=500, null=True,choices = CLASS_CHOICE)

	def __str__(self):
		return self.user_name.username

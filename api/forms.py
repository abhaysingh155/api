from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from datetime import datetime, timedelta 


class CreateUserForm(UserCreationForm):
	age = forms.IntegerField(required=True)
	city = forms.CharField(max_length=12, min_length=4, required=True,)
	grade = forms.CharField(max_length=4, min_length=1, required=True,) 
	board = forms.CharField(max_length=4, min_length=4, required=True,)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'age', 'city', 'grade', 'board' ]

class DocumentForm(forms.ModelForm):
	date_choice= (
			(datetime.now().strftime('%d-%m-%Y'),'Today'),
			((datetime.now() + timedelta(1)).strftime('%d-%m-%Y'), 'Tomorrow'),
			((datetime.now() + timedelta(2)).strftime('%d-%m-%Y'), (datetime.now() + timedelta(2)).strftime('%d-%m-%Y')),
		)
	time_choice=(
			('11:00 AM','11:00 AM'),
			('12:00 PM','12:00 PM'),
			('1:00 PM','1:00 PM'),
			('2:00 PM','2:00 PM'),
			('3:00 PM','3:00 PM'),
			('4:00 PM','4:00 PM'),
			('5:00 PM','5:00 PM'),
			('6:00 PM','6:00 PM'),
			('7:00 PM','7:00 PM'),
			('8:00 PM','8:00 PM'),
			('9:00 PM','9:00 PM'),
		)

	date= forms.ChoiceField(choices = date_choice)
	time= forms.ChoiceField(choices = time_choice)
	class Meta:
		model = Trial_Class
		fields = ( 'date', 'time')

from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from .models import *
from .forms import CreateUserForm, DocumentForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')

		context = {'form':form}
		return render(request, 'api/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'api/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	return render(request, 'api/learning_page.html')

@login_required(login_url='login')
def trial_classes(request, user_name):
   name=Trial_Class.objects.filter(user_name=user_name)
   try:
      assert(name[0])
   except:
       if request.method == 'POST':
          form = DocumentForm(request.POST, request.FILES )
          if form.is_valid():
             job=form.save(commit=False)
             job.user_name=request.user
             job.save()
             name=Trial_Class.objects.filter(user_name=user_name)
             return render(request, 'api/learning_page.html',{"name":name,})
       else:
          form = DocumentForm()
       return render(request, 'api/learning_page.html', {'form': form, "schedule_trial": True })
   else:
      return render(request, 'api/learning_page.html',{"name":name,})

@login_required(login_url='login')
def upcoming_classes(request, user_name):
	get_class=Assign_Classes.objects.filter(user_name=user_name)
	try:
		assert(get_class[0])
	except:
		information = "Hey %s, No class has been assigned to you yet !" % str(user_name).upper()
		return render(request, 'api/learning_page.html',{"information":information,})
	else:
		return render(request, 'api/learning_page.html',{"get_class":get_class,})

@login_required(login_url='login')
def practice_questions(request, user_name):
	get_question=Assign_Questions.objects.filter(user_name=user_name)
	try:
		assert(get_question[0])
	except:
		info_question = "Hey %s, No question has been assigned to you yet !" % str(user_name).upper()
		return render(request, 'api/learning_page.html',{"info_question":info_question,})
	else:
		return render(request, 'api/learning_page.html',{"get_question":get_question,})





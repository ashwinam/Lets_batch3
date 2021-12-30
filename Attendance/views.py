from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Mark_Attendance, MasterData
from .forms import StudentForm,StudentForm1, MasterForm,MarkAttednaceForm, OneStudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user

import time 


def about(request):
	return HttpResponse("<h1>Hello World</h1>")

def home(request):
	context = {'title': 'Project'}
	return render(request, 'Attendance/base.html', context )
	

def name(request):
	return HttpResponse("<h1>Hello Ashwin</h1>")

posts = [{

	'roll_num': 20,
	'Name':"abc" ,
	'email' : "Abc@xyz.com"},

	{	'roll_num': 30,
	'Name':"nmb" ,
	'email' : "NMB@xyz.com"},   ]

def DataDsiplay(request):
	context = {'data' : posts}
	return render(request, 'Attendance/table.html', context )

def DataDsiplayStudent(request):
	posts = Student.objects.all()
	context = {'data' : posts}
	return render(request, 'Attendance/displaytable.html', context )

def student_form_data(request):
	form = StudentForm()
	context = {'form': form}
	if request.method=='POST':
		form = StudentForm(request.POST)
		try :
			print ("hello",form.is_valid())
			if form.is_valid():
				ID = form.cleaned_data.get('ID')
				name = form.cleaned_data['name']
				email = form.cleaned_data['email']
				Class1 = form.cleaned_data['Class']
				Student.objects.create(stuid=ID,stuname=name,stumail=email,stuclass=Class1)
				messages.success(request,f"Record added for {name}")
				#return render(request,'Attendance/success.html', {'name':name})
			else:
				messages.warning(request,f"Error in the form")
		except Exception as e :
			print ("error",e)

	return render(request,'Attendance/displayforms.html', context)

def student_form_data_model(request):
	form = StudentForm1()
	context = {'form': form}
	if request.method=='POST':
		form = StudentForm1(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['stuname']
			messages.success(request,f"Record added {name}")
		else:
			messages.warning(request,f"Error in the form")
	return render(request,'Attendance/displayforms.html', context)

# Create your views here.
'''
@login_required(login_url='Login')
def master_Data(request):     # writeable 
	if request.user.groups.exists():
		if request.user.groups.all()[0].name=='grp_write':
			form = MasterForm()
			context = {'form': form, 'legend': "Enter the Details "}

			if request.method=='POST':
				form = MasterForm(request.POST)
				if form.is_valid():
						try :
						
							form.save()
							name = form.cleaned_data['stuname']
							messages.success(request,f"Record added {name}")
						except Exception as e :
							messages.warning(request,f"{e}")
				else:
					print (type(form.errors))
					messages.warning(request,f"{form.errors}", )

			return render(request, 'Attendance/displayforms.html', context)
		else :
			return HttpResponse("<h1>You are not Authorized</h1>")
	else :
		return HttpResponse("<h1>You are not Authorized</h1>")
'''
@login_required(login_url='Login')
@allowed_user(allowed_roles=['grp_write'])
def master_Data(request):     # writeable 
			form = MasterForm()
			context = {'form': form, 'legend': "Enter the Details "}

			if request.method=='POST':
				form = MasterForm(request.POST)
				if form.is_valid():
						try :
						
							form.save()
							name = form.cleaned_data['stuname']
							messages.success(request,f"Record added {name}")
						except Exception as e :
							messages.warning(request,f"{e}")
				else:
					print (type(form.errors))
					messages.warning(request,f"{form.errors}", )

			return render(request, 'Attendance/displayforms.html', context)

def e_h(t1):
	t9 = time.localtime(t1)
	return time.strftime("%d-%m-%Y-%H", t9)

def Mark_Att(request):
			form = MarkAttednaceForm()
			context = {'form': form, 'legend': "Mark Your Attendance"}
			if request.method=='POST':
				form = MarkAttednaceForm(request.POST)
				if form.is_valid():
					mark1 = form.save(commit=False)
					mark1.time1 = int(time.time())
					mark1.ip_address = request.META.get('REMOTE_ADDR')
					mark1.platform = request.META.get('HTTP_USER_AGENT')
					mark1.date1 = e_h(mark1.time1)
					form.save()
					messages.success(request,f"Attedance Marked")
					print ("OKKKK")


			return render(request,'Attendance/displayforms.html', context)
'''
def display_attendance(request):
	if request.user.groups.exists():
		allowed_roles = ['grp1_read', 'grp_write']
		n_g = request.user.groups.all()[0].name
		if n_g in allowed_roles:
			posts = Mark_Attendance.objects.all()
			context = {'data' : posts}
			return render(request, 'Attendance/displayatt.html', context )
		else :
			return HttpResponse("<h1>You are not Authorized</h1>")
	else :
		return HttpResponse("<h1>You are not Authorized</h1>")
'''
@allowed_user(allowed_roles=['grp_write','grp1_read'])
def display_attendance(request):
			posts = Mark_Attendance.objects.all()
			context = {'data' : posts}
			return render(request, 'Attendance/displayatt.html', context )


@login_required(login_url='Login')
def Mark_Att(request):
	form = OneStudentForm()
	context = {'form': form, 'legend': "Enetr the UID"}

	if request.method=='POST':
		form = OneStudentForm(request.POST)
		if form.is_valid():
			try :
				id1=  (form.cleaned_data.get('ID'))
				m1=MasterData.objects.filter(stuid=id1)[0]
				posts = Mark_Attendance.objects.filter(uid=m1)
				context = {'form': form, 'legend': "Enetr the UID",'data' : posts}
				
				return render(request, 'Attendance/oneatt.html', context )
			except IndexError:
				messages.warning(request,f"UID is not Present")
			except Exception as e :
				messages.warning(request,f"{e}, {type(e)}")

	return render(request,'Attendance/oneatt.html', context)

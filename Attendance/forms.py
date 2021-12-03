from django import forms 
from .models import Student, MasterData,Mark_Attendance

class StudentForm(forms.Form):  # here forms is a module and Form is class 
	ID = forms.CharField(max_length=100)
	name = forms.CharField(max_length=100, label="NAME")
	email = forms.CharField(max_length=100)
	Class = forms.CharField(max_length=100)  


	def clean_name(self):
		valname = self.cleaned_data['name']
		print ("valname&&&&&&&&&&",valname)
		if len(valname)<4:
			raise forms.ValidationError("Enter more than or equal to 4")
		return valname


class StudentForm1(forms.ModelForm):

	class Meta:
		model = Student
		fields = ['stuid','stuname','stumail','stuclass']


class MasterForm(forms.ModelForm):
	class Meta:
		model = MasterData
		fields = ['stuid','stuname','stumail','subject']

class MarkAttednaceForm(forms.ModelForm):
	class Meta:
		model = Mark_Attendance
		fields = ['uid','subject_name']

class OneStudentForm(forms.Form):  # here forms is a module and Form is class 
	ID = forms.IntegerField()
	
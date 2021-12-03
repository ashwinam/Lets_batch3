from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def Profile(request):
	return render(request,'user_app/profile.html')

def loginPage(request):
	form = AuthenticationForm()
	context = {'form': form,'legend' : 'Login Now' }

	next = ""
	if request.GET:
		next = request.GET['next']

		
	if request.method =='POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request,username=username, password=password)  # matches the password 
			if user is not None:
				login(request,user)  # session creation 
				if next=="":
					return redirect('profile')
				else:
					return redirect(next)


			else:
				messages.warning(request,"Username or password is incorrect")



	return render(request,'user_app/login.html', context)


from django.shortcuts import render
import random

# Create your views here.

def home(request):
	return render(request,"generator/home.html", )




def password(request):

	mypassword = ''
	characters = list('abcdefghijklmnopqrstuvwxz')

	if request.GET.get('Uppercase'):
		characters.extend('ABCDEFGHIJKLMNOPQRSTUV') 

	if request.GET.get('numbers'):
		characters.extend('0123456789')

	if request.GET.get('Special'):
		characters.extend('!@$%^&*?/>.<,')

	length = int(request.GET.get('length',12))


	for i in range(length):
		mypassword += random.choice(characters)
	
	return render(request,'generator/password.html', {'password':mypassword})

	


def about(request):
	return render(request,'generator/about_password.html',)
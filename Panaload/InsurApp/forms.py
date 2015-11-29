from django import forms
from .models import MicroInsuranceUsers
from django.contrib.auth import authenticate, login
from .models import UnderWriter
from .models import Insurance
from .models import Branch
# from .models import Employee

class LoginForm(forms.ModelForm):

	username = forms.CharField( widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Enter Username'}))

	password = forms.CharField(widget=forms.PasswordInput(attrs={'class ':'form-control','placeholder' : 'Enter Password'}))

	class Meta: 
		model = MicroInsuranceUsers
		fields = ['username','password']

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Sorry, user does not exist!")
		return self.cleaned_data

	def login(self,request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user

class AvailInsuranceForm(forms.ModelForm):
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Enter First Name'}))
	middlename = forms.CharField(widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Enter Middle Name'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Enter Last Name'}))
	contactno = forms.CharField(widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Contact No.'}))


	class Meta:
		model = MicroInsuranceUsers




	
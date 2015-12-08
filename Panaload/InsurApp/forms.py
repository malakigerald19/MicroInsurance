
from django import forms
from .models import MicroInsuranceUsers
from django.contrib.auth import authenticate, login
from .models import UnderWriter
from .models import Insurance
from .models import Branch
from .models import CustomerAvail
from functools import partial
import datetime
import re
from functools import partial
# from .views import home_page_frontline
# from .models import Employee
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
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
	DATE_FORMATS = [
    '%Y-%m-%dT%H:%M:%S-%z',
	]
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Enter First Name'}))
	middlename = forms.CharField(required = False,widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Enter Middle Name'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Enter Last Name'}))
	contactno = forms.CharField(widget=forms.TextInput(attrs={'class ':'form-control','placeholder' : 'Contact No.'}))
	# date = forms.DateField(
 #          widget=DateTimePicker(options={"format": "YYYY-MM-DD",
 #                                         "pickTime": False}))
	error_css_class = 'error'

	class Meta:
		model = CustomerAvail
		fields = ['firstname','middlename','lastname','contactno']

	def clean(self):
		contactno = self.cleaned_data.get('contactno')
		if re.match('^(09|\+639|)\d{9}$',contactno): 
			print (contactno)
			# raise forms.ValidationError("Password should be a combination of Alphabets and Numbers")
		else:
			raise forms.ValidationError("Contact Number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")
		return contactno
	def __init__(self, *args, **kwargs):
	    super(AvailInsuranceForm, self).__init__(*args, **kwargs)
	    self.fields['firstname'].label = "First Name:"
	    self.fields['middlename'].label = "Middle Name:"
	    self.fields['lastname'].label = "Last Name:"
	    self.fields['contactno'].label = "Contact No:"
	    # self.fields['firstname'].label = "First Name:"

	# def __init__(self, *args, **kwargs):
	# 	print(insuranceapplied)
	# def clean(self):
	# def __init__(self, *args, **kwargs):
 #        other_variable = kwargs.pop('other_variable')
 #        super(MyForm, self).__init__(*args, **kwargs)

	
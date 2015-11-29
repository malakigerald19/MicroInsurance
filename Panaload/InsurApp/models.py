from django.db import models
import datetime
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from django.core.exceptions import ValidationError
from django.forms import TextInput, Textarea
from decimal import Decimal
# Create your models here.

Higher =None
STATUS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
)
USRTYPE = (
        ('M', 'Manager'),
        ('F', 'FrontLiner'),
        ('F', 'UnderWriter'),

)
class MicroInsuranceUsers(models.Model):
	username = models.CharField(max_length=120,blank=False)
	password = models.CharField(max_length=120,blank=False)
	usertype = models.CharField(max_length=120,blank=False,choices=USRTYPE)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True,null=True)

	def __str__(self):
		return self.username,self.usertype

class UnderWriter(models.Model):
	
	phone_regex = RegexValidator(regex=r'^(09|\+639|)\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")
	UnderWriterName = models.CharField(verbose_name="Underwriter Name:",max_length=200,blank=False)
	UnderWriterAddress = models.CharField(verbose_name="Underwriter Address:",max_length=500,blank=False,default='')
	UnderWriterContactNo = models.CharField(verbose_name="UnderWriter Contact No.:",max_length=14,default='',validators=[phone_regex])
	UnderWriterStatus = models.CharField(verbose_name="Status",max_length=10,choices=STATUS,default='Active')
	def __str__(self):
		return str(self.UnderWriterName)

	class Meta:
		verbose_name_plural ='Under Writers'

class Insurance(models.Model):
	def get_deadline():
   	 return datetime.datetime.now() + timedelta(days=20)
	InsuranceSKU = models.CharField(verbose_name="Insurance Name:",max_length=200, blank=False)
	InsuranceBasePrice = models.DecimalField(verbose_name="Insurance Base Price:",max_digits=10,decimal_places=2,default=Decimal(0))
	InsuranceSellingPrice = models.DecimalField(verbose_name="Insurance Selling Price:",max_digits=10,decimal_places=2,default=Decimal(0))
	InsuranceAmount = models.DecimalField(verbose_name="Insured Amount:",max_digits=10,decimal_places=2,blank=False,default=Decimal(0))
	InsuranceValidity = models.IntegerField(verbose_name="Insurance Validity(days):",default='7',blank=False)
	InsuranceAgeMin = models.IntegerField(verbose_name="Minimum Age:",default='18',blank=False,validators=[MinValueValidator(18),
                                       MaxValueValidator(115)])
	InsuranceAgeMax = models.IntegerField(verbose_name="Maximum Age:",default='100', blank=False)
	InsuranceLimit = models.IntegerField(verbose_name="Limit Per Person:",default='3',blank=False)
	InsuranceEffectiveFrom = models.DateField(verbose_name="Valid From:",default=datetime.date.today,blank=False)
	InsuranceEffectiveTo = models.DateField(verbose_name="Valid To:",blank=False,default=get_deadline)
	UnderWriter = models.ForeignKey(UnderWriter,default='')

	class Meta:
		ordering = ('id',)
		unique_together = ('InsuranceSKU', 'UnderWriter')
		verbose_name_plural = 'Insurances'

	def __str__(self):
		return self.InsuranceSKU

	def clean(self):

		if self.InsuranceAgeMin > self.InsuranceAgeMax:
			raise ValidationError('Maximum Age should be Greater than Minumum Age')

		if self.InsuranceBasePrice > self.InsuranceSellingPrice:
			raise ValidationError('Base Price should be Greater than Selling Price ')

		if self.InsuranceEffectiveFrom > self.InsuranceEffectiveTo:
			raise ValidationError('Valid To should be Greater than Valid From')

# class Employee(models.Model):

#     # phone_regex = RegexValidator(regex=r'^(09|\+639|)\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")
#  	phone_regex = RegexValidator(regex=r'^(09|\+639|)\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")
#  	EmployeeName = models.CharField(max_length=200, blank=False)
#  	EmployeeType = models.CharField(max_length=50,blank=False,choices=EMPTYPE,default='Active')
#  	EmployeeContactNo = models.CharField(max_length=12,validators=[phone_regex])
#  	EmployeeStatus = models.CharField(verbose_name="Status:",max_length=10,choices=STATUS,default='Active')
#     # UnderWriterStatus = models.CharField(verbose_name="Status",max_length=10,choices=STATUS,default='Active')
#  	def __str__(self):
#  		return self.EmployeeName

#  	class Meta:
#  		verbose_name = 'Employees'



class Branch(models.Model): 
	phone_regex = RegexValidator(regex=r'^(09|\+639|)\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")
	BranchName = models.CharField(verbose_name="Branch Name:",max_length=200, blank=False)
	BranchAddress = models.CharField(verbose_name="Branch Address:",max_length=1000,blank=False,default='')
	BranchContactNo = models.CharField(verbose_name="Branch Contact No.:",max_length=13, default='',validators=[phone_regex])
	# BranchManager = models.ForeignKey(Employee,default='')

	class Meta:
		verbose_name_plural = 'Branches'

	def __str__(self):
		return self.BranchName






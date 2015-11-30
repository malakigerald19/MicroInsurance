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
        ('U', 'UnderWriter'),

)


class UnderWriter(models.Model):
	
	phone_regex = RegexValidator(regex=r'^(09|\+639|)\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")
	UnderWriterName = models.CharField(verbose_name="Underwriter Name:",max_length=200,blank=False)
	UnderWriterAddress = models.CharField(verbose_name="Underwriter Address:",max_length=500,blank=False,default='')
	UnderWriterContactNo = models.CharField(verbose_name="UnderWriter Contact No.:",max_length=13,default='',validators=[phone_regex])
	UnderWriterStatus = models.CharField(verbose_name="Status",max_length=10,choices=STATUS,default='Active')
	def __str__(self):
		return str(self.UnderWriterName)

	class Meta:
		verbose_name_plural ='Under Writers'
		unique_together = ('UnderWriterName','UnderWriterAddress','UnderWriterContactNo')
		ordering = ('id',)

class Insurance(models.Model):
	def get_deadline():
   	 return datetime.datetime.now() + timedelta(days=7)
	InsuranceSKU = models.CharField(verbose_name="Insurance Name:",max_length=200, blank=False)
	InsuranceBasePrice = models.DecimalField(verbose_name="Insurance Base Price:",max_digits=10,decimal_places=2)
	InsuranceSellingPrice = models.DecimalField(verbose_name="Insurance Selling Price:",max_digits=10,decimal_places=2)
	InsuranceAmount = models.DecimalField(verbose_name="Insured Amount:",max_digits=10,decimal_places=2,blank=False)
	InsuranceValidity = models.IntegerField(verbose_name="Insurance Validity(days):",blank=False)
	InsuranceAgeMin = models.IntegerField(verbose_name="Minimum Age:",blank=False,validators=[MinValueValidator(18),
                                       MaxValueValidator(115)])
	
	InsuranceAgeMax = models.IntegerField(verbose_name="Maximum Age:", blank=False)
	InsurancePolicy = models.TextField(verbose_name = "Insurance Policy:",blank=False,default='')
	InsuranceLimit = models.IntegerField(verbose_name="Limit Per Person:",blank=False)
	InsuranceEffectiveFrom = models.DateField(verbose_name="Valid From:",default=datetime.date.today,blank=False)
	InsuranceEffectiveTo = models.DateField(verbose_name="Valid To:",blank=False,default=get_deadline)
	UnderWriter = models.ForeignKey(UnderWriter,default='')

	class Meta:
		ordering = ('id',)
		# unique_together = ('InsuranceSKU', 'UnderWriter')
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
	BranchStatus = models.CharField(verbose_name="Status",max_length=10,choices=STATUS,default="Active")
	class Meta:
		verbose_name_plural = 'Branches'
		ordering = ('id',)
		unique_together = ('BranchName', 'BranchAddress', 'BranchContactNo')

	def __str__(self):
		return self.BranchName

class CustomerAvail(models.Model):
	phone_regex = RegexValidator(regex=r'^(09|\+639|)\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxxx'. Up to 13 digits allowed.")
	CustomerFName = models.CharField(verbose_name="First Name", max_length = 50, blank=False )
	CustomerMName = models.CharField(verbose_name="Middle Name", max_length = 50,blank=True,null=True)
	CustomerLName = models.CharField(verbose_name="Last Name", max_length = 50, blank = False)
	CustomerContactNo = models.CharField(verbose_name="Contact No",max_length=13,blank=False,validators=[phone_regex],default='')
	InsuranceApplied = models.ForeignKey(Insurance,default='',verbose_name="Insurance Applied:",null=True)
	timestamp = models.DateTimeField(verbose_name="Date Registered",auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True,null=True)
	branch = models.ForeignKey(Branch,default='',verbose_name="Branch",blank=True,null=True)

	class Meta:
		verbose_name_plural = "Customer Info and Insurances"
		ordering = ('id',)
		# unique_together = ('CustomerFName','CustomerMName','CustomerLName','InsuranceApplied')


	def __str__(self):
		return (self.CustomerFName + ' ' + self.CustomerMName + ' ' + self.CustomerLName)

class MicroInsuranceUsers(models.Model):
	username = models.CharField(max_length=120,blank=False)
	password = models.CharField(max_length=120,blank=False)
	status = models.CharField(verbose_name="Status",max_length=10,choices=STATUS,default="Active")
	usertype = models.CharField(max_length=120,blank=False,choices=USRTYPE)
	name = models.CharField(max_length=120,blank="False",null=False, verbose_name="Name")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True,null=True)
	branch = models.ForeignKey(Branch,default='',verbose_name="Branch",null=True,blank=True)
	underwriter = models.ForeignKey(UnderWriter,verbose_name="UnderWriter",default='',null=True,blank=True)
	


	def __str__(self):
		return self.username

	class Meta:
		verbose_name_plural = "Micro Insurance Users"
		ordering = ('id',)





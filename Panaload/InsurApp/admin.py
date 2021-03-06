from django.contrib import admin
from .models import MicroInsuranceUsers
from .models import UnderWriter
from .models import Insurance
from .models import Branch
from .models import CustomerAvail
# from .models import Employee




class SignUpAdmin(admin.ModelAdmin):
	list_display = ("__str__","usertype","timestamp","updated")


	class Meta:
		model = MicroInsuranceUsers
	class Media:
		js = (
			'//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'js/category-field-admin.js',)


class CreateUnderWriter(admin.ModelAdmin):
	list_display = ("__str__","UnderWriterStatus")
	class Meta:
		model = UnderWriter	

class CreateInsurance(admin.ModelAdmin):
	list_display = ("__str__","UnderWriter")
	class Meta:
		model = Insurance


class CreateBranch(admin.ModelAdmin):
	list_display = ("__str__","BranchAddress")
	class Meta:
		model = Branch

class TransactCustomer(admin.ModelAdmin):
	list_display = ("__str__", "InsuranceApplied")
	class Meta:
		model = CustomerAvail

# class CreateManager(admin.ModelAdmin):
# 	list_display = ("__str__","EmployeeStatus")
# 	class Meta:
# 		model = Employee

# Register your models here.
admin.site.register(MicroInsuranceUsers,SignUpAdmin)
admin.site.register(UnderWriter,CreateUnderWriter)
admin.site.register(Insurance,CreateInsurance)
admin.site.register(Branch,CreateBranch)
admin.site.register(CustomerAvail,TransactCustomer)
# admin.site.register(Employee,CreateManager)
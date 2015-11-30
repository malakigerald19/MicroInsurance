from django.shortcuts import render
from .forms import LoginForm, AvailInsuranceForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import MicroInsuranceUsers, CustomerAvail,Insurance
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render
from django.template import Context
from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import Insurance
from django import forms

BRANCH = None
    # no object satisfying query exists
insuranceapplied= None
def login_user(request):
    state = "Please log in below..."
    username = request.POST.get('username')
    password = request.POST.get('password')
    form = LoginForm(request.POST or None)
    if MicroInsuranceUsers.objects.filter( username = username, password = password ,status ='A', usertype = 'M').exists():
    	return HttpResponseRedirect('/managerhome/')
    elif MicroInsuranceUsers.objects.filter(username = username, password = password, status ='A', usertype = 'F').exists():
        BRANCH = MicroInsuranceUsers.objects.filter(InsuranceSKU=availedinsurance).values_list('InsuranceLimit').first()
        return HttpResponseRedirect('/frontlinehome/')
    elif MicroInsuranceUsers.objects.filter(username = username, password = password, status ='A', usertype = 'U').exists():
        return HttpResponseRedirect('/underwriterhome/')
    		#return render(request,"homepage.html")
    return render_to_response('login.html',{'state':state, 'username': username, 'form': form},context_instance=RequestContext(request))

def home_page_frontline(request):

    form = AvailInsuranceForm(data=request.POST )
    firstname = request.POST.get('firstname')
    middlename = request.POST.get('middlename')
    lastname = request.POST.get('lastname')               
    contactno = request.POST.get('contactno')
    insurance_list = Insurance.objects.all()
    insuranceapplied = request.POST.get('insurances')
    holder = "--Choose Insurance Here--"
    error = "•Please Choose an Insurance"
    limit =""
    if insuranceapplied == holder:
       print("A")
    else:
        error = ""
        if form.is_valid():
            firstname = request.POST.get('firstname')
            middlename = request.POST.get('middlename')
            lastname = request.POST.get('lastname')               
            contactno = request.POST.get('contactno')
            availedinsurance= Insurance.objects.get(InsuranceSKU=insuranceapplied)
            insuranceSKULimit = Insurance.objects.filter(InsuranceSKU=availedinsurance).values_list('InsuranceLimit').first()
            print (insuranceSKULimit[0])
            # int1 , int2 = insuranceSKULimit
            chklimit = CustomerAvail.objects.filter(CustomerFName=firstname,CustomerMName=middlename,CustomerLName=lastname,CustomerContactNo=contactno,InsuranceApplied=availedinsurance).count()
            print(chklimit)

            if chklimit >= insuranceSKULimit[0]:
                limit = "Insurance Limit has been reached!"
            else:
                limit =""
                customeravail = CustomerAvail(CustomerFName=firstname,CustomerMName=middlename,CustomerLName=lastname,CustomerContactNo=contactno,InsuranceApplied=availedinsurance)
                customeravail.save()
                form = AvailInsuranceForm()

    return render_to_response('homepage.html', {'form': form, 'insurance_list': insurance_list , 'error': error, 'limit': limit},context_instance=RequestContext(request))
	# return render_to_response('homepage.html',{'form': form},context_instance=RequestContext(request))


# def request_page(request):
# 	title = "Page"
# 	context = {

# 			"title": title,
			
# 	}
# 	username = forms.CharField()
# 	password = forms.CharField()

# 	if(request.GET('submitlgn')):
# 		if MicroInsuranceUsers.objects.filter(username='username', password='password').exists():	
# 			return render_to_response("home.html",context)
# 		else:
# 			return render_to_response("home.html",{})
# 	return render_to_response("home.html",{})
# # def login(request):
# # 	if request.method == "POST"
		
# # @login_required
# # def home_page(request):
# #     return render_to_response(
# #     'login.html',
# #     { 'user': request.user }
# #     )
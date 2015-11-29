from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import MicroInsuranceUsers
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

    # no object satisfying query exists

def login_user(request):
    state = "Please log in below..."
    username = request.POST.get('username')
    password = request.POST.get('password')
    # usertype = request.POST.get('usertype')
    manager = 'gerald'
    status = "Active"
    underwriter = "UnderWriter"
    frontline = "FrontLiner"
    form = LoginForm(request.POST or None)
    if MicroInsuranceUsers.objects.filter( username = username, password = password ,status ='A', usertype = 'M').exists():
    	return HttpResponseRedirect('/managerhome/')
    elif MicroInsuranceUsers.objects.filter(username = username, password = password, status ='A', usertype = 'F').exists():
        return HttpResponseRedirect('/frontlinehome/')
    elif MicroInsuranceUsers.objects.filter(username = username, password = password, status ='A', usertype = 'U').exists():
        return HttpResponseRedirect('/underwriterhome/')
    		#return render(request,"homepage.html")
    return render_to_response('login.html',{'state':state, 'username': username, 'form': form},context_instance=RequestContext(request))

def home_page_frontline(request):
	return render(request, 'homepage.html')

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
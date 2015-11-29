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




def login_user(request):
    state = "Please log in below..."
    username = request.POST.get('username')
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
    	user = form.login(request)
    	if user:
    		login(request,user)
    		return HttpResponseRedirect('/home/')
    		#return render(request,"homepage.html")
    return render_to_response('login.html',{'state':state, 'username': username, 'form': form},context_instance=RequestContext(request))
    # if request.POST and form.is_valid():
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = form.login(request)
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             state = "You're successfully logged in!"
    #             return render(request,"home.html")
    #         else:
    #             state = "Your account is not active, please contact the site admin."
    #     else:
    #         state = "Your username and/or password were incorrect."

    # return render_to_response('login.html',{'state':state, 'username': username, 'form': form},context_instance=RequestContext(request))

def home_page(request):
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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	# url(r'^$', 'InsurApp.views.home_page', name='login'),
	#url(r'^$', 'InsurApp.views.login_user', name='home'),
	url(r'^frontlinehome/$', 'InsurApp.views.home_page_frontline', name='frontlinehome'),
    url(r'^$', 'InsurApp.views.login_user'),

  ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

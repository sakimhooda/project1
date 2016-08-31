from django.conf.urls import include, url
from . import views

urlpatterns = [	
	url('register/$',views.registration),
	url('logout$',views.logout),
	
	url('type/(?P<id>[0-9]+)/$',views.sortacrdtype),
	url('internin/(?P<id>[0-9]+)/$',views.sortacrdinternin),
	url('(?P<id>[0-9]+)/$',views.showintern),
	
	
	url('$',views.welcome),
	
    
]
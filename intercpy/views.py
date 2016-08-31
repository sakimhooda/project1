from django.shortcuts import render
from .forms import login,register
from .models import pi,Sex,internshiptype,internshipin,internships
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse


def sortacrdtype(request,id):
	if 'email' in request.session:
		email=request.session['email']
		d=pi.objects.get(email=email)
		name=d.name
		data=internships.objects.all().filter(interntype_id=id)
		type=internshiptype.objects.all()
		internin=internshipin.objects.all()
		return render(request,'intercpy/type.html',{'name':name,'type':type,'internin':internin,'data':data})
	else:
		return HttpResponseRedirect('http://127.0.0.1:8000')
	


def sortacrdinternin(request,id):
	if 'email' in request.session:
		email=request.session['email']
		d=pi.objects.get(email=email)
		name=d.name
		data=internships.objects.all().filter(internarea_id=id)
		type=internshiptype.objects.all()
		internin=internshipin.objects.all()
		return render(request,'intercpy/type.html',{'name':name,'type':type,'internin':internin,'data':data})
	else:
		return HttpResponseRedirect('http://127.0.0.1:8000')




def showintern(request,id):
	if 'email' in request.session:
		email=request.session['email']
		d=pi.objects.get(email=email)
		name=d.name
		d=internships.objects.get(pk=id)
		type=internshiptype.objects.all()
		internin=internshipin.objects.all()
		return render(request,'intercpy/include.html',{'name':name,'d':d,'type':type,'internin':internin})
	else:
		
		return HttpResponseRedirect('http://127.0.0.1:8000')
		
	

def logout(request):
	del request.session['email']
	request.session.modified = True
	return HttpResponseRedirect('http://127.0.0.1:8000')

def registration(request):
	
	f1=register()
	if request.method == 'POST':
		f1=register(request.POST)
		
		if f1.is_valid():
			name=f1.cleaned_data['name']
			sex=f1.cleaned_data['sex']
			dob=f1.cleaned_data['dob']
			email=f1.cleaned_data['email']
			password=f1.cleaned_data['password']
				
			try:
				user=pi.objects.get(email=email)
			except ObjectDoesNotExist:
				user='-1'
			if user=='-1':
				f=pi(name=name,sex=sex,dob=dob,email=email,password=password)
				f.save()
				msg='go to <a href="http://127.0.0.1:8000">log in </a>page"'
				return HttpResponse(msg)
			else:
				
				return render(request,'intercpy/register.html',{'f1':f1,'msg':msg})
		else:
			msg='every field is required'
			return render(request,'intercpy/register.html',{'f1':f1,'msg':msg})
			
			
						
			
	else:
		return render(request,'intercpy/register.html',{'f1':f1})

def welcome(request):
	data=internships.objects.all()
	type=internshiptype.objects.all()
	internin=internshipin.objects.all()
	
	if 'email' in request.session:
		email=request.session['email']
		d=pi.objects.get(email=email)
		name=d.name
		
		return render(request,'intercpy/base.html',{'email':email,'name':name,'data':data,'type':type,'internin':internin})
	f2=login()
	
	if request.method == 'POST':
		f2=login(request.POST)
		#return render(request,'intercpy/register.html',{'f2':f2})
		if f2.is_valid() :
			
			email=f2.cleaned_data['email']
			password=f2.cleaned_data['password']
			try:
				user=pi.objects.get(email=email , password=password)
			except ObjectDoesNotExist:
				user='-1'
			if user=='-1':
				msg='email or password is worng'
				return render(request,'intercpy/welcom.html',{'f2':f2,'msg':msg})
			else:
				request.session['email']=email
				d=pi.objects.get(email=email)
				name=d.name
				
				return render(request,'intercpy/base.html',{'email':email,'name':name,'data':data,'type':type,'internin':internin})
				
						
			
	else:
		
		
		return render(request,'intercpy/welcom.html',{'f2':f2})

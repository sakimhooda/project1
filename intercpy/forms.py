from .models import pi
from django import forms


class register(forms.ModelForm):
	class Meta:
		model=pi
		fields=['name','sex','dob','email','password']
		widgets={'password':forms.PasswordInput(),
		}
		labels={'name':('USERNAME'),'sex':('SEX'),'dob':('DATE OF BIRTH'),'email':('EMAIL'),'password':('PASSWORD')
		}
	
class login(forms.ModelForm):
	class Meta:
		model=pi
		fields=['email','password']
		widgets={'password':forms.PasswordInput()
		}
		labels={'email':('EMAIL'),'password':('PASSWORD')
		}
		
from django import forms
from .models import ExpressIt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ExpressItForm(forms.ModelForm):
	class Meta:
		model=ExpressIt
		fields=['name','description','location','image']

''' we can also set help_text of fields by help_text='Optional.' '''
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)


    '''set help_text of fields to None'''
    def __init__ (self, *args, **kwargs):
    	super(UserCreationForm, self).__init__(*args, **kwargs)

    	for fieldname in ['username','password2']:
    		self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
	username=forms.CharField(label='User Name', max_length=64)
	password=forms.CharField(widget=forms.PasswordInput())



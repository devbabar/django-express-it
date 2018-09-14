from django.contrib import messages
from django.shortcuts import render, get_object_or_404, Http404,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ExpressIt
from .forms import ExpressItForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def index(request):
	all_data   = ExpressIt.objects.all().select_related('user')
	expressits = all_data.order_by('-timestamp')[:6]

	if (len(expressits) > 3) and (len(expressits) < 6):
		expressits = expressits[:3]
	else:
		expressits = expressits[:6]

	context = {
			'expressits':expressits
	}

	return render(request,"index.html", context)

'''------------------------------------------
check the given username is already takeh
------------------------------------------'''

def validate_username(request):
    username=request.GET.get('username',None)
    data = {
        'is_taken':User.objects.filter(username__iexact=username).exists()
    }

    if data['is_taken']:
        data['error_message'] = "A username is already taken, please try other."
    return JsonResponse(data)
'''------------------------------------------
------------------------------------------'''

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			u=form.cleaned_data['username']
			p=form.cleaned_data['password']
			user=authenticate(username=u, password=p)
			if user is not None:
				if user.is_active:
					login(request,user)
					messages.success(request,"You have been successfully logged in. Welcome back {}".format((user.username).capitalize()))
					return HttpResponseRedirect('/')
			else:
				messages.error(request,"The username or password were incorrect, Try Again")
				return HttpResponseRedirect('/accounts/login/')
	else:
		form=LoginForm()
		return render(request, 'login.html',{'form':form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def detail(request,expressit_id):
	expressit=ExpressIt.objects.get(id=expressit_id)
	return render(request,'detail.html',{'expressit':expressit})
		
	
@login_required
def post_expressit(request):
	if request.method == 'POST':
		form=ExpressItForm(request.POST,request.FILES)
		if form.is_valid():
			ExpressIt=form.save(commit=False)
			ExpressIt.user=request.user
			ExpressIt.save()
			return HttpResponseRedirect('/')
	else:
		form = ExpressItForm()
	return render(request, 'post.html',{'form':form})


@login_required
def profile(request,username):
	user=User.objects.get(username=username)
	if request.user == user:
		expressits=ExpressIt.objects.filter(user=user)
		return render(request,'profile.html',{'expressits':expressits, 'user':user})
	else:
		messages.warning(request,"Sorry, You are not allowed to see this profile.")
		# return HttpResponse ("sorry")
		return HttpResponseRedirect('/')


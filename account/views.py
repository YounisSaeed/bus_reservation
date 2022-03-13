from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
#from .decoretors import unauthenticated_user# Create your views here.
from django.contrib.auth.models import User , Group
from django.contrib.auth import login , authenticate , logout 
from .forms import CreationUserForm
from django.contrib import messages
from .decoretors import unauthenticated_user

# Create your views here.
def home(request):
    return render(request,'account/home.html')

######################### Login#######################
@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.groups.filter(name="passanger").exists():
                return redirect('/passanger/list')
            else:
                messages.warning(request,'username or password not correct')
                return redirect('login')
    
    context = {}    
    return render(request,'account/login.html',context)

########################## Register ########################
@unauthenticated_user
def Register_page(request):
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            username = form.cleaned_data.get('username')
            user = form.save()
            group = Group.objects.get(name='passanger')
            user=form.save()
            user.groups.add(group)
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Created For ' + user)
            return redirect('login')
    else:
        form = CreationUserForm()
    context = {'form':form}
    return render(request,'account/signup.html',context)


######################### LogOut ########################
def log_out(request):
    logout(request)
    return redirect('login')
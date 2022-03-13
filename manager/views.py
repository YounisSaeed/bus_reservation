from urllib import request, response
from django.http import HttpResponseNotModified
from django.shortcuts import redirect, render , get_object_or_404 , HttpResponseRedirect
from .models import Trip 
from passanger.models import Book
from django.contrib import messages
from account.decoretors import allowed_users , unauthenticated_user
from django.contrib.auth.decorators import login_required
from .forms import TripForm,BookForm
# Create your views here.

########################### List Trip with Admin ###########

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def list_trips(request):
    data = Trip.objects.all().filter(author=request.user.id)
    return render(request,'manager/list_bus.html',{'data':data})


########################## Delete Trip from Admin ##################


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def delete_trip(request,id):
    obj = get_object_or_404(Trip, id = id)
    tit = obj.company_name
    try:

        if obj.delete():
            messages.success(request,f'trip \" {tit} \" has been deleted !!')
            return redirect('/manager/list')
    except Trip.DoesNotExist:
        return redirect('/manager/list')


###################### Trip Details with Recepts passangers #########


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def trip_details(request,id):
    objs = Trip.objects.get(id=id)
    recets = Book.objects.filter(trip_id=id)
    book_number = Book.objects.filter(trip_id=id,status='APPROVED').count()
    pending = Book.objects.filter(trip_id=id,status='pending').count()
    return render(request,'manager/details.html',{'data':objs , 'recet' : recets , 'number':book_number,'pending':pending,'r':recets})


####################### Create Trip For Admin #######################


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def create_trip(request):
    if request.method=='POST':
        form = TripForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author=request.user
            new_form.save()
            return redirect('/manager/list')

    else:
        form = TripForm()
    context={
        'form':form
    }
    return render(request,'manager/create.html',context)

   
##############################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def edit_trip(request,id):
    data = Trip.objects.get(id=id)
    form = TripForm(instance=data)
    if request.method=='POST':
        form = TripForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/manager/list')
    else:
        form = TripForm(instance=data)
    return render(request,'manager/edit_trip.html',{'travel':data})

#############################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def search_recet(request):
    if request.method=='POST':
        searched = request.POST['searched']
        recet_number = Book.objects.filter(recet_number__contains=searched)
    return render(request,'manager/search_recet.html',{'searched':searched, 'BOOKS':recet_number})
#############################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def change_status(request,id):
    data=Book.objects.get(id=id)
    if request.method=='POST':
        data.status = 'APPROVED'
        try:
            if data.save():
                return redirect('/manager/list')
        except Book.DoesNotExist:
            return redirect('/manager/list')
    return render(request,'manager/recet.html',{'recets':data})
################################################################

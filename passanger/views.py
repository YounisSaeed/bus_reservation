from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from manager.models import Trip
from passanger.models import Book
from account.decoretors import allowed_users , unauthenticated_user
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['passanger'])
def list_trips(request):
    trip = Trip.objects.all()
    return render(request,'passanger/list.html',{'trip':trip})
################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['passanger'])
def trip_detial(request,id):
    trp = Trip.objects.get(id=id)
    context={'trip':trp}
    return render(request,'passanger/details.html',context)
###################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['passanger'])
def book_trip(request):
    if request.method=='POST':
        id_trip = request.POST.get('trip_id')
        trip = Trip.objects.get(id=id_trip)
        author = request.user
        # auth=Book.objects.get(author=author)
        # rand = auth.recet_number
        # stat = auth.status
        use = Book.objects.create(author=author,trip_id=trip)
        context={"book":use}
        return render(request,'passanger/invoice.html',context)

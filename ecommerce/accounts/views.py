from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from  .models import *
from .form import OrderForm, CreateUserForm, LoinUserForm, CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_user, admin_only
# Create your views here. 
@login_required(login_url='login')
@admin_only
def index(request):
    last_5order=Order.objects.all().order_by('-id')[:5]
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_order=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    contex = {'orders':orders,'customers':customers,'total_order':total_order,'delivered':delivered,'pending':pending,'last_5order':last_5order}
    return render(request, 'accounts/dashboard.html',contex)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def user(request):
   
    orders=request.user.customer.order_set.all()
    total_order=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    contex = {'orders':orders,'total_order':total_order,'delivered':delivered,'pending':pending,}
    return render(request, 'accounts/user.html',contex)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def user_account(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
    products=Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    total_order=orders.count()
    myFilter=OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs
    context={'customer':customer,'orders':orders,'total_order':total_order,'myFilter':myFilter}
    return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def create_order(request):
    form = OrderForm()
    if request.method=='POST':
        #request.POST=request.POST.copy()
        #request.POST['status']='Delivered'
        customer=request.POST.get('customer')
        form = OrderForm(request.POST) 
        if form.is_valid():
           order=form.save()
           return redirect(reverse('customer', args=[customer]))
    context={'form':form}
    return render(request, 'accounts/create_order.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update_order(request, pk):
    order=Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method=='POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
           form.save()
           return redirect('/') 

    context={'form':form}
    return render(request, 'accounts/create_order.html',context) 


def delete_order(request, pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
           order.delete()
           return redirect('/') 

    context={'order':order}
    return render(request, 'accounts/delete_order.html',context) 

@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                group=Group.objects.get(name='customer')
                user.groups.add(group)
                name=request.POST.get('username')
                email=request.POST.get('email')
                Customer.objects.create(user=user,name=name,email=email)
                messages.success(request,'You May login now',extra_tags='success')
                return redirect('login')
        context={'form':form}
        return render(request, 'accounts/register.html',context) 
@unauthenticated_user
def loginPage(request):
    
    form=LoinUserForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login success full',extra_tags='success')
            previous_page=request.META.get('HTTP_REFERER')
            return redirect('/')
        else:
            messages.success(request,'Wrong username or password',extra_tags='error')
            return redirect('login') 
    context={'form':form}
    return render(request, 'accounts/login.html',context) 
    
def logoutPage(request):
    logout(request)
    return redirect('/login')
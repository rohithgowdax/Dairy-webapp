from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

class  CategoryView(View):
    def get(self, request, value):
        product = Product.objects.filter(category = value)
        title = Product.objects.filter(category = value).values('title')
        return render(request,"category.html",locals())
    
class CategoryTitle(View):
    def get(self, request, value):
        product = Product.objects.filter(title = value)
        title = Product.objects.filter(category = product[0].category)
        return render(request, "category.html", locals())
    

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(id = pk) 
        return render(request,'productdetail.html',locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request,"signup.html",locals())
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Succesfully Please Login")
        else:
            messages.warning(request,"Invalid data Inputs! ")
        return render(request,"signup.html",locals())
    
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request,'profile.html',locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Created Succesfully")
        else:
            messages.warning(request,"Invalid data Inputs! ")
        return render(request,'profile.html',locals())

def adress(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())
            
class UpdateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'updateaddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile Updated Succesfully")
        else:
            messages.warning(request,"Invalid data Inputs! ")
        return redirect('address')
        


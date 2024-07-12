from django.shortcuts import render
from django.views import View
from .models import Product
from .forms import CustomerRegistrationForm
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
            messages.success(request,"Succes")
        else:
            messages.warning(request,"Invalid data ")
        return render(request,"signup.html",locals())
            

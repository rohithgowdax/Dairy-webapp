from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Cart,Payment,OrderPlaced
from .forms import *
import razorpay
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required

# displays no .of items in cart
def cart_num(request)->int:
    if request.user.is_authenticated:
        return  len(Cart.objects.filter(user=request.user))


# Create your views here.
def home(request):
    cartitem = cart_num(request)
    #
    return render(request, "index.html",locals())

def about(request):
    cartitem = cart_num(request)
    # 
    return render(request, "about.html",locals())

def contact(request):
    cartitem = cart_num(request)
    # 
    return render(request, "contact.html",locals())

class  CategoryView(View):
    def get(self, request, value):
        cartitem = cart_num(request)
        # 
        product = Product.objects.filter(category = value)
        title = Product.objects.filter(category = value).values('title')
        return render(request,"category.html",locals())
    
class CategoryTitle(View):
    def get(self, request, value):
        cartitem = cart_num(request)
        # 
        product = Product.objects.filter(title = value)
        title = Product.objects.filter(category = product[0].category)
        return render(request, "category.html", locals())
    

class ProductDetail(View):
    def get(self, request, pk):
        cartitem = cart_num(request)
        # 
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
            return redirect('login')
        else:
            messages.warning(request,"Invalid data Inputs! ")
        return render(request,"signup.html",locals())

class ProfileView(View):
    def get(self, request):
        cartitem = cart_num(request)
        # 
        form = CustomerProfileForm()
        return render(request,'profile.html',locals())

    def post(self, request):
        cartitem = cart_num(request)
        # 
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode).save()
            
            return redirect('address')
        else:
            messages.warning(request,"Invalid data Inputs! ")
        return render(request,'profile.html',locals())

@login_required
def adress(request):
    cartitem = cart_num(request)
    # 
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())

def delete_address(request,pk):
    Customer.objects.get(id=pk).delete()
    return redirect('address')
    
class UpdateAddress(View):
    def get(self,request,pk):
        cartitem = cart_num(request)
        #
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
        
@login_required
def Logout(request):
     logout(request)
     return redirect('login')

@login_required(login_url='login')
def add_to_cart(request):
    
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('showcart')


@login_required
def showcart(request):
    cartitem = cart_num(request)
    # 
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount+=value
    totalamount = amount +40
    return render(request,'cart.html',locals())

@login_required
def pluscart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount+=value
        totalamount = amount +40
        data={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount':totalamount
        }
        return JsonResponse(data)
    
@login_required   
def minuscart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity >1:
            c.quantity-=1
            c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount+=value
        totalamount = amount +40
        data={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount':totalamount
        }
        return JsonResponse(data)
    
def removecart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        cart = Cart.objects.filter(user=request.user)
        amount = 0.0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount+=value
        totalamount = amount +40
        data={
                'quantity':c.quantity,
                'amount':amount,
                'totalamount':totalamount
        }
        return JsonResponse(data)
      

class CheckoutView(View):

    def get(self, request):
        cartitem = cart_num(request)
        # 
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount+= value
        totalamount = famount + 40
        
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data = { "amount": razoramount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment_response = client.order.create(data=data)
        
        # {'amount': 13000, 'amount_due': 13000, 'amount_paid': 0, 'attempts': 0, 'created_at': 1721752898, 'currency': 'INR', 'entity': 'order', 'id': 'order_Oc8wXBE8KwPkxf', 'notes': [], 'offer_id': None, 'receipt': 'order_rcptid_11', 'status': 'created'}
        order_id = payment_response['id']
        order_status =payment_response['status']
        if order_status == 'created':
            payment = Payment(user = user, 
                              amount =totalamount, 
                              razorpay_order_id = order_id,
                              razorpay_payment_status = order_status)
            payment.save()
        
        return render(request,"checkout.html",locals())
    
@login_required    
def paymentdone(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')
    # print(f'payment done oid ={order_id, }, pid ={payment_id}, cid = {cust_id}')
    user = request.user
    customer = Customer.objects.get(id=cust_id)

    # To update payment status and payment id 
    payment =Payment.objects.get(razorpay_order_id=order_id)
    payment.paid =True
    payment.razorpay_order_id= order_id
    payment.razorpay_payment_id= payment_id

    payment.save()

    # to save order details
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment,cust_id = customer.id).save()
        c.delete()
    return redirect('orders')

@login_required
def orders(request):
    cartitem = cart_num(request)
    # 
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request,"orders.html",locals())

def search(request):
    query = request.GET['search']
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "search.html",locals())
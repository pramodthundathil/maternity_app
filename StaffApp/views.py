from django.shortcuts import render,redirect
from Home.forms import UserAddForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from Bookings.models import Booking
from Patient.models import PatientProfile,TreatmetHistory
from Doctor.models import DoctorList
from django.http import HttpResponse
from .models import Bills, Product, CartItems, CheckoutItems
from .forms import ProductAddForm
from django.contrib.auth.decorators import login_required


import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponseBadRequest

razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.
def AddStaff(request):
    form = UserAddForm()
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')

            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('AddStaff')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('AddStaff')
            
            else:
                new_user = form.save()
                group = Group.objects.get(name='staff')
                new_user.groups.add(group) 
                new_user.save()
                
                messages.success(request,"Staff Created Successfully...")
                return redirect('AddStaff')
    context = {
        'form':form,
    
    }
    return render(request,"staff/addstaff.html",context)

def StaffIndex(request):
    bookings = Booking.objects.all()
    context = {
        "bookings":bookings
    }
    return render(request,"staff/staffhome.html",context)


def BookingView(request,pk):
    group = request.user.groups.all()[0].name
    booking = Booking.objects.filter(id = pk)
    bookingget = Booking.objects.get(id= pk)
    Patient = PatientProfile.objects.filter(PatientId = bookingget.user )
    Patient1 = PatientProfile.objects.get(PatientId = bookingget.user )
    treatment = TreatmetHistory.objects.filter(Patient = Patient1)
    context = {
        "group":group,
        "booking":booking,
        "Patient":Patient,
        "lenpa":Patient.count(),
        "pk":pk,
        "treatment":treatment
        
    }
    if group == "staff":
        return render(request,"staff/patientprofile.html",context)
    elif group == "doctor":
        return render(request,"doctor/patientprofile.html",context)
    else:
        return HttpResponse("<h2 style='color:orange;text-align:center'>You are not autherise to view This Page</h2>")

def AddPatientProfile(request,pk):
    if request.method == "POST":
        pname = request.POST['pname']
        place = request.POST['place']
        phone = request.POST['pnum']
        treat = request.POST["trment"]
        bookingget = Booking.objects.get(id= pk)
        
        profile = PatientProfile.objects.create(PatientName = pname,Place = place,PhoneNumber = phone,Treatment = treat,PatientId = bookingget.user,Doctor = bookingget.Doctor)
        profile.save()
        messages.info(request,"Profile Updated")
    return redirect('BookingView',pk=pk)

def UpdateProfile(request,pk,sk):
    if request.method == "POST":
        profile = PatientProfile.objects.get(id=pk)
        
        profile.PatientName = request.POST["pname"]
        profile.Place = request.POST["place"]
        profile.PhoneNumber = request.POST["pnum"]
        profile.Treatment = request.POST["trment"]
        profile.save()
        messages.info(request,"Profile Updated")
    return redirect('BookingView',pk = sk)

def PatientList(request):
    group = request.user.groups.all()[0].name
    profile = PatientProfile.objects.all()
    context = {
        "profile":profile
    }
    if group == "staff":
        return render(request,"staff/patientview.html",context)
    elif group == "doctor":
        return render(request,"doctor/patientview.html",context)
    else:
        return HttpResponse("<h2 style='color:orange;text-align:center'>You are not autherise to view This Page</h2>")
        

def DeleteProfile(request,pk):
    PatientProfile.objects.get(id = pk).delete()
    messages.info(request,"Profile Deleted")
    return redirect('PatientList')

def DoctorView(request):
    doctor = DoctorList.objects.all()
    context = {
        "doctor":doctor
    }
    return render(request,"staff/doctorview.html",context)


def BillView(request):
    group = None
    if request.user.groups.all().exists():
        group = request.user.groups.all()[0].name
        
    if group == "staff":
        context = {
            "bill":Bills.objects.all()
            }
        return render(request,"staff/bills.html",context)
    else:
        context = {
            "bill":Bills.objects.filter(user = request.user)
        }
        return render(request,"bills.html",context)
        

def AddBill(request,pk):
    if request.method == "POST":
        book = Booking.objects.get(id = pk)
        amt = request.POST['amt']
        bill = Bills.objects.create(Billamount = amt, user = book.user)
        bill.save()
        messages.info(request,"Bill Added")
    return redirect("BookingView", pk=pk)

def AddProduct(request):
    form = ProductAddForm()
    product = Product.objects.filter(user = request.user)
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            med  = form.save()
            med.user = request.user
            med.save()
            messages.info(request,"Data saved")
            return redirect("AddProduct")

        else:
            messages.info(request,"Not done..")
            return redirect("AddProduct")
        
    context = {
        "form":form,
        "product":product,
    }
    return render(request,"staff./products.html",context)

def DeleteProduct(request,pk):
    product = Product.objects.get(id = pk)
    product.image.delete()
    product.delete()
    messages.info(request,"Product Deleted")
    return redirect("AddProduct")


@login_required(login_url='SignIn')
def CartPage(request):
    cart = CartItems.objects.filter(user = request.user)
    total = 0
    for item in cart:
        total = total + item.price
    gst = total*18/100
    price = total - gst
    context = {
        "cart":cart,
        "total":total,
        "gst":gst,
        "price":price,
        'totalcart':len(cart)
    }
    return render(request,"cartpage.html",context)


@login_required(login_url='SignIn')
def AddToCart(request,pk):
    medicine = Product.objects.get(id = pk)    
    cart = CartItems.objects.create(product = medicine,user = request.user,stock = 1,price = medicine.MRP )
    cart.save()
    return redirect('CartPage')
        
    
@login_required(login_url='SignIn')
def IncreaseQuantity(request,pk):
    cart = CartItems.objects.get(id = pk)
    cart.stock = cart.stock + 1
    cart.price = cart.price + cart.product.MRP
    cart.save()
    return redirect('CartPage')

@login_required(login_url='SignIn')
def DecreaseQuantity(request,pk):
    cart = CartItems.objects.get(id = pk)
    
    if cart.stock == 1:
        cart.delete()
    else:
        cart.stock = cart.stock - 1
        cart.price = cart.price - cart.product.MRP
        cart.save()
        
    return redirect('CartPage')

@login_required(login_url='SignIn')
def DeleteCartItem(request,pk):
    cart = CartItems.objects.get(id = pk)
    cart.delete()
    return redirect('CartPage')



@login_required(login_url='SignIn')
def ProceedCheckout(request):
    cart = CartItems.objects.filter(user = request.user)
    for i in cart:
        Checkoutitems = CheckoutItems.objects.create(product = i.product,user=request.user,stock = i.stock,price = i.price,status = "item Ordered")
        Checkoutitems.save()
        dcart = CartItems.objects.get(id = i.id)
        dcart.delete()
    checkitems = CheckoutItems.objects.filter(user = request.user,payment_status = False)
    total = 0
    for item in checkitems:
        total = total + item.price
    currency = 'INR'
    amount = total * 100 # Rs. 200
    context = {}

  # Create a Razorpay Order Pyament Integration.....
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))

  # order id of newly created order.
    razorpay_order_id = razorpay_order["id"]
    callback_url = "paymenthandler/"

  # we need to pass these details to frontend.
    
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url 
    context['slotid'] = "1",
    context['numitems'] = len(checkitems)
    context['total'] = total
    # context['amt'] = (product1.Product_price)*float(qty)
    
    return render(request,'checkoutpage.html',context)


@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

      # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                checkitems = CheckoutItems.objects.filter(user = request.user,payment_status = False)
                total = 0
                for item in checkitems:
                    total = total + item.price
                    checkitems.payment_status = True
                    checkitems.save()
                amount = total * 100 # Rs. 200
                try:
                    print("working 1")
                    razorpay_client.payment.capture(payment_id, amount)
                    return redirect('Success1')
          # render success page on successful caputre of payment
                except:
                    print("working 2")
                    return redirect('Success1')
                    
                    
          # if there is an error while capturing payment.
            else:
                return render(request, 'paymentfail.html')
        # if signature verification fails.    
        except:
            return HttpResponseBadRequest()
        
      # if we don't find the required parameters in POST data
    else:
  # if other than POST request is made.
        return HttpResponseBadRequest()
    
def Success1(request):
    return render(request,'Paymentconfirm.html')

@login_required(login_url='SignIn')
def MyOrderes(request):
    orderitems = CheckoutItems.objects.filter(user=request.user)
    context = {
        "orderitems":orderitems
    }
    return render(request,'myorders.html',context)

def deleteordercus(request,pk):
    CheckoutItems.objects.filter(id=pk).delete()
    return redirect("CustomerOrderes")

def CustomerOrderes(request):
    items = CheckoutItems.objects.all()
    context = {
        "items":items
    }
    return render(request,"staff/orders.html",context)

def deleteordermanu(request,pk):
    CheckoutItems.objects.get(id = pk).delete()
    return redirect("CustomerOrderes")


    


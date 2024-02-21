from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image, Contact
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import razorpay
from django.core.mail import send_mail
from .forms import ContactForm




def home(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                img_instance = form.save(commit=False) 
                img_instance.user = request.user  
                img_instance.save()  
                form = ImageForm()
                return HttpResponseRedirect('/index')
        else:  
            form = ImageForm()
            img = Image.objects.all()

        return render(request, 'home.html', {'img':img ,'form': form})

    else:
        return redirect("/")

    
def register(request):
    context={}
    if request.method == "POST":
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        try:
            if uname == '' or upass == '' or ucpass == '':
                context['error'] = "Please fill all the fields"
                return render(request, "registration.html", context)
            elif upass!=ucpass:
                context['error'] = "Passwords do not match"
                return render(request, "registration.html", context)
            else:
                user_obj = User.objects.create(password=upass,username=uname,email=uname)
                user_obj.set_password(upass)
                user_obj.save()
                return HttpResponseRedirect( "/")
        except:
            return HttpResponse("This user is already registered")
    else:
        return render(request, "registration.html")


def user_login(request):
    context={}
    if(request.method=="POST"):
        uname=request.POST['uname']
        upass=request.POST['upass']
        if uname=='' or upass=='':
            context['error']="please fill all the details"
            return render(request, "login.html",context)
        else:               
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return HttpResponseRedirect("/index/")
            else:
                context['error']="Invalid cridential"
    return render(request, "login.html",context)





def makepayment(request):
    client = razorpay.Client(auth=("rzp_test_j0tKbvuWvct0uB", "IvRYWaqSB2skK0IU9X7EP3GX"))
    data = { "amount": 150000, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    print(payment)
    context={}
    context['payment']=payment
    return render(request,"premium.html",context)


def senduseremail(request):
    send_mail(
    "thoughtfull life and mind",
    "started premium sucessfully",
    "26sahanikaambre@gmail.com",
    ["rohanrrandive@gmail.com"],
    fail_silently=False,
)
    return redirect("/")


def contactform(request):
    if request.method == 'POST':
            # Handle form data here, e.g., save to database, send email, etc.
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            obj=Contact.objects.create(name=name, email=email, message=message)
            obj.save()
            # Redirect after successful form submission
            return render(request, 'contact.html')    
    else:
        return render(request, 'contact.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")


    








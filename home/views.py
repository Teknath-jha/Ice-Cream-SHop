from django.shortcuts import render ,HttpResponse, redirect
# for contact def 
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
import razorpay
from .models import FilesAdmin

# Create your views here.


def index(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    context={
        'variable1' : "this is 1st sent",
        'variable2' : "this is 2st sent",
        'variable3' : "this is 3st sent",
        'variable4' : "this is 4st sent",
        'variable5' : "this is 5st sent",
    }
    return render(request,'index.html',context)
    # return HttpResponse("This page is first called by  project urls  from where it sends to app home's urls.py  and from here it sends to views of home and then matched  a function in views and then executes done finally mera janjal sulaj gaya thanks to harry....Also this is not a html page  THIS IS A HttpResponse great...")

# till here don't find difference between view n request 
def interest(request):
    pass
    # return HttpResponse("Great you have a defined path rather than like home   Also this is not a html page  THIS IS A HttpResponse great...")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This a about page end point is only mentioned in home.urls but not in project's urls...  THIS IS A HttpResponse great...")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This a service page end point is only mentioned in home.urls but not in project's urls...  THIS IS A HttpResponse great...")

def gift(request):
    return render(request,'gift.html')
    # return HttpResponse("This a gift  page end point is only mentioned in home.urls but not in project's urls...  THIS IS A HttpResponse great...")



def contact(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email   =request.POST.get('email')
        contact =request.POST.get('contact')
        # desc    =request.POST.get('desc')
        password=request.POST.get('password')

        contact = Contact(username=username , email= email , contact = contact  ,password = password , date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details successfully sent!')
    return render(request,'contact.html')
    # return HttpResponse("This a contact page end point is only mentioned in home.urls but not in project's urls...  THIS IS A HttpResponse great...")


# login
def loginuser(request):
    print('inside loginuser')
   
    if request.method == "POST":
        print('fetching info')
        username = request.POST.get('username')
        # email = request.POST.get('email')
        print('fetching info of usrname')
        password = request.POST.get('password')
        print('fetching info of password')

        user = authenticate(username=username  , password=password)
        
        if user is not None:
            login(request, user)
            print('logged in user')
            messages.success(request, 'logged in successful!')
            return render(request,'index.html')
        else:
            messages.success(request, 'OOPs invalid credentials!')
            return render(request,'login.html')
    return render(request,'login.html')

def logoutuser(request):
    messages.success(request,'You have successfully logged out!!!')
    logout(request)
    return render(request,'contact.html')

def registeruser(request):
    print('in register')
    if request.method == 'POST':
        username=request.POST.get('username')
        email   =request.POST.get('email')
        contact =request.POST.get('contact')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            print('in if of register')
            messages.warning(request, "Account with this Username  already exists.")
            return render(request, 'register.html')
        elif User.objects.filter(email=email).exists():
            print('in elif of register')
            messages.warning(request, "Account with this email  already exists.")
            return render(request, 'register.html')
        else:
            print('in else of register')
            user = User.objects.create_user(username=username ,first_name=first_name, last_name=last_name , email= email ,password = password  )
            user.save()
            user1 = Contact(username=username , email= email , contact=contact , date=datetime.today() )
            user1.save()
            print('registered')
            messages.success(request,"Successfully registered!")
            return redirect('/login')
 
    return render(request , 'register.html')


def profileuser(request):
    contact=Contact.objects.filter(username=request.user.username)[0].contact
    print(contact)
    context={
        'contact' : contact,
    }
    return render(request,'profile.html',context)




# Not working 
def changePassword(request):
    if request.method =='POST':
        newPassword = request.POST.get('password2')
        U=User.objects.get(username=request.user.username)
        U.set_password(newPassword)
        U.save()
        update_session_auth_hash(request,U)
        print('saved password')
        messages.success(request,'Password changed successfully!!!')
        return render(request,'login.html')
    return render(request,'profile.html')

# ----------------------------------     RAZORPAY SETTING-------------------------------------------------

def razorPay(request):
    print('in razorPay')
    if request.method=='POST':
        print('if of razorpay')
        amount = 100
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_agtBEf4PEspMpI','lqytfEwvzRIAkft3FEekzi1B'))
        payment=client.order.create({'amount':amount , 'currency':'INR', 'payment_capture':'1'})
        return render(request,'paymentDone.html')
    print('out of if')
    return render(request,'raZorpay.html')



def success(request):
    return rendor(request,'login.html')


# ----------------------------------     RAZORPAY SETTING ENDS -------------------------------------------------

# ----------------------------------     Downloading images-------------------------------------------------------


def home(request):
    context={'file':FilesAdmin.objects.all()}
    return render(request,'home.html',context)

def download(request):  
    print('in download views')
    file_path=os.path.join(settings.MEDIA_ROOT,path)    
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['content-Disposition']='inline;filename='+os.path.basename(file_path)
            print('image is returning')
            return response
    raise Http404



# ----------------------------------     Downloading images ends -------------------------------------------------
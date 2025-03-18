from django.shortcuts import render,redirect
from datetime import datetime
from .models import *
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import logging ##logger

logger = logging.getLogger('django')

# Create your views here.

def home(request):
    try:
        cate = Category.objects.all() 
        momo = Momo.objects.all() 
        cateid = request.GET.get('Category')
        if cateid:
            momo = Momo.objects.filter(Category=cateid)
        else:
            momo = Momo.objects.all()


        if request.method=='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            try:
                user = Contact(namemodel=name,emailmodel=email,phonemodel=phone,messagemodel=message)
                user.full_clean()
                user.save()
                messages.success(request,f'{name} form submitted successfully')
                return redirect('home')
            except Exception as e:
                print(message)
                messages.error(request,f'{str(e)}')
                return redirect('home')
    except Exception as e:
        logger.error(str(e),exc_info=True)

    context = {
        'date':datetime.now(),
        'cate':cate,
        'momo' : momo,
        }
    return render(request,'main/index.html',context)

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name)
        try:
            user = Contact(namemodel=name,emailmodel=email,phonemodel=phone,messagemodel=message)
            user.full_clean()
            user.save()
               ###### send mail #########
            subject = "welcome Message"
            message = render_to_string('main/gmail_format.html',{'name':name,'date':datetime.now()})
            from_email = 'saraswotikhadka2k2@gmail.com'
            recipient_list = [email] ##current database store submit
        # send_mail(subject,message,from_email,recipient_list)
            emailmsg = EmailMessage(subject,message,from_email,recipient_list)
            emailmsg.attach_file('main/static/images/c_momo.jpg')
            emailmsg.send(fail_silently=True)
            print(email)
            messages.success(request,f'{name} form submitted successfully')
            return redirect('contact')
        except Exception as e:
            messages.error(request,f'{str(e)}')
            return redirect('contact')
    return render(request,'main/contact.html',{'date':datetime.now()})

@login_required(login_url='login')
def about(request):
    date = datetime.now()
    return render(request,'main/about.html',{'date':date})

@login_required(login_url='login')
def menu(request):
    date = datetime.now()
    return render(request,'main/menu.html',{'date':date})

@login_required(login_url='login')
def services(request):
    date = datetime.now()
    return render(request,'main/services.html',{'date':date})
    
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'username is not register yet')
            return redirect('login')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if remember:
                request.session.set_expiry(120000000)
            else:
                request.session.set_expiry(0)
            next = request.POST.get('next','')
            return redirect(next if next else 'home')
        else:
            messages.error(request,'invalid password!')
            return redirect('login')
    next = request.GET.get('next','')
    return render(request,'auth/login.html',{'next':next})

def register(request):
    if request.method=='POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        u_name = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:
            try:
                # validate starts
                validate_password(password)
                if password==u_name:
                    messages.error(request,"password and username shouldn't be the same")
                    return redirect('register')
                if User.objects.filter(username=u_name).exists():
                    messages.error(request,'username already exists')
                    return redirect('register')
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exists')
                    return redirect('register')
                if not re.search(r'[A-Z]',password):
                    messages.error(request,'password should contain at least one upper letter')
                    return redirect('register')
                if not re.search(r'\d',password):
                    messages.error(request,'password should at least contain one number')
                    return redirect('register')
                if not re.search(r'\W',password):
                    messages.error(request,'password should at least contain one special character')
                    return redirect('register')
                
                User.objects.create_user(first_name=f_name,last_name=l_name,username=u_name,email=email,password=password)
                messages.success(request,'Register successfully')
                return redirect('login')
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request,error)
                return redirect('home')
            # validation ends
        else:
            messages.error(request,'password and confirm password not same')
            return redirect ('register')
    return render(request,'auth/register.html')

def Terms(request):
    return render(request,'main/Terms.html')

def support(request):
    return render(request,'main/support.html')

def privacy(request):
    return render(request,'main/privacy.html')

def policy(request):
    return render(request,'main/policy.html')

def log_out(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'auth/change_password.html',{'form':form})


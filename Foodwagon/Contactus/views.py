from django.shortcuts import render,redirect
from .models import *
import smtplib, ssl
from Service.models import Parent_Type

from django.contrib.auth.decorators import login_required

from home.decorators import unauthenticated_user
# Create your views here.

@login_required(login_url='login')
def email(request):
     if request.method=='POST':
            name=request.POST['name']
            reciever_email=request.POST['email']
            number=request.POST['mobile']
            sub=request.POST['subject']
            body="A message was sent to you by "+name+" using email: "+reciever_email+" and mobile no: "+number+". It said: \n"+request.POST['body']

            about=Email.objects.all()[0]
            
            sender_email=about.email
            password=about.password

            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                #Email must allow Secondary Applications
                smtp.login(sender_email,password)

                msg=f'Subject:{sub}\n\n{body}'
                smtp.sendmail('email',sender_email,msg)

                message=Message.objects.all()[0].body
                sub="Message Recieved By DarkLight"
                body='Dear '+name+',\n'+message+'\n Yours Truly,\n'+about.name+',\nLegal24By7'
                msg=f'Subject:{sub}\n\n{body}'
                
                smtp.sendmail('email',reciever_email,msg)

     else:
        return redirect('home')

def help(request):
    helps=Help.objects.all()
    types=Type.objects.all()
    parent_types=Parent_Type.objects.all()

    context={
        'types':types,
        'helps':helps,
        'parent_types':parent_types,
    }

    return render(request,"contactus/help.html",context)
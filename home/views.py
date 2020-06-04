from django.shortcuts import render,redirect
import smtplib, ssl
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):

    sliders=Slider.objects.all()
    services=Services.objects.all()
    about=About.objects.all()[0]
    #about.color=str.lower(about.color)
    images=GalleryImage.objects.all()
    links=Link.objects.all()
    context={
        'sliders':sliders,
        'services':services,
        'about':about,
        'images':images,
        'links':links,
    }
    return render(request,"index.html",context)

def mail(request):

    if request.method=='POST':
        name=request.POST['name']
        reciever_email=request.POST['email']
        sub=request.POST['subject']
        body="A message was sent to you by "+reciever_email+". It said: \n"+request.POST['body']

        about=About.objects.all()[0]
        
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

            sub="Message Recieved By DarkLight"
            body='Dear '+name+', This is to notify that your message has been recieved by DarkLight Photography.'
            msg=f'Subject:{sub}\n\n{body}'
            
            smtp.sendmail('email',reciever_email,msg)
            
    return redirect('/')
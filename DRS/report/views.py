from django.shortcuts import render,redirect
import datetime
from .models import News,NewsType,Other,OtherType
# Create your views here.
def index(request):
        news=News.objects.all()
        newstype=NewsType.objects.all()
        other=Other.objects.all()
        othertype=OtherType.objects.all()
        return render(request,'index.html',{'news':news,'newstype':newstype,'others':other,'othertypes':othertype})

def report(request):
        if request.method=='POST':
                news=News()
                news.pub_date=datetime.datetime.now()
                news.title=request.POST.get('title')
                news.desc=request.POST.get('desc')
                news.image=request.POST.get('img')
                nt=NewsType()
                nt.sect="Local"
                news.sect = nt
                nt.save()
                news.save()
        
        return redirect(request,'index.html')

                
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from Court.models import Cases
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect("/")
def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            cases=Cases.objects.all()
            auth.login(request,user)
            return render(request,"lawyer.html",{'cases':cases})
        else:
            print("User not found")
            return redirect("login")
    else:
        print("User not found")
        return render(request,'login.html')


def register(request):

    if request.method=='POST':
        first_name=request.POST['First_name']
        last_name=request.POST['Last_name']
        email=request.POST['Email']
        user=request.POST['User']
        password=request.POST['Password']
        conf_pass=request.POST['Conf_Pass']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user,password=password,email=email)
        user.save()
        print("User Created")
        return redirect('/')

    else:
        print("User not Created")
        return render(request,'register.html')
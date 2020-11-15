from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone
from urllib.parse import quote_plus
from .forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):

    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404

    form=PostForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save() 
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context={
        "title":"Create a Post",
        "form":form
    }
    return render(request,"post_form.html",context)

def post_detail(request,id=None):
    instance=get_object_or_404(Post,id=id)
    if instance.draft or instance.publish>timezone.now().date():
        if not request.user.is_superuser or not request.user.is_staff:
            raise Http404

    share_string=quote_plus(instance.content)
    context={
        "title":instance.title,
        "object":instance,
        "share_string":share_string,
    }
    return render(request,"post_detail.html",context)    

def post_list(request):
    queryset_list=Post.objects.active()

    if request.user.is_staff or request.user.is_superuser:
        queryset_list=Post.objects.all()

    query=request.GET.get("query")
    if(query):
        queryset_list=queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)).distinct()

    paginator = Paginator(queryset_list, 10) # Show 10 contacts per page.
    pagereqvar='page'
    page = request.GET.get(pagereqvar)
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)

    context={
        "title":"Latest Feed",
        "page_request_var":pagereqvar,
        "object_list":queryset
    }
    return render(request,"post_list.html",context)

def post_update(request,id=None):

    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404


    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    

    context={
        "title":instance.title,
        "instance":instance,
        "form":form
    }
    return render(request,"post_form.html",context)    

def post_delete(request,id=None):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("posts:list")
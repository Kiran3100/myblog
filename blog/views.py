from django.shortcuts import render,HttpResponseRedirect
from blog.forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from blog.forms import PostForm,UpdateAdminProfileForm,UpdateUserProfileForm
from blog.models import PostModel
from django.core.paginator import Paginator
from blog.forms import PostForm
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    data = PostModel.objects.all()
    paginator = Paginator(data,4)
    pageno = request.GET.get('page')
    pageobj = paginator.get_page(pageno)
    context = {'pageobj':pageobj,'count':paginator.count,'user':request.user}
    return render(request,'blog/home.html',context)

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account has been created')
            return  HttpResponseRedirect('/blog/login')
    else:
        form = SignupForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
            else:
                messages.success(request,'User is Not Found')
        else:
            form = AuthenticationForm()
        return render(request,'blog/login.html',{'form':form})
    
    else:
        return HttpResponseRedirect('/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateUserProfileForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'Profile Updated Successfully...!')
        else:
            if request.user.is_superuser == True:
                form = UpdateAdminProfileForm(instance=request.user)
            else:
                form = UpdateUserProfileForm(instance=request.user)
        context = {'form':form}
        return render(request,'blog/profile.html',context)
    else:
        return HttpResponseRedirect('/')
    
    
def dashboard(request):
    pass


def user_logout(request):
    logout(request)
    messages.success(request,'Logout Successfully...!')
    return HttpResponseRedirect('/')

def userinfo(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        form = UpdateAdminProfileForm(instance=user)
        return render(request,'blog/userinfo.html',{'form':form})
    else:
        return HttpResponseRedirect('/blog/login')

def user_changepwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password Changed Successfully....!')
                return HttpResponseRedirect('/blog/profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'blog/changepwd.html',{'form':form})
    else:
        return HttpResponseRedirect('/blog/login')
    
def set_user(request):
    return render(request,'blog/home.html',{"username":username}) 
   
def get_user(request):
    return render(request,'blog/home.html',{'username':username})
    

def post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                form = PostForm()
                messages.success(request,'Posted')
            else:
                print('Invalid data')
        else:
            form = PostForm()
        return render(request,'blog/post.html',{'form':form})
    else:
        return HttpResponseRedirect('/blog/login')

def update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = PostModel.objects.get(id=id)
            form = PostForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/blog/dashboard')
        else:
            data = PostModel.objects.get(id=id)
            form = PostForm(instance=data)
        return render(request,'blog/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/blog/dashboard')

def about(request):
    pass

def contact(request):
    pass
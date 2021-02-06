from django.shortcuts import render,redirect
from FoodApp.models import FoodModel,ReviewModel
from FoodApp.forms import CreateReviewForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Home(request):
    today = datetime.date.today()
    itemlist = FoodModel.objects.filter(createdon__year=today.year, createdon__month=today.month, createdon__day=today.day)
    context = {
        "itemlist" : itemlist
    }
    return render(request,'FoodApp/home.html',context)

@login_required(login_url="login")
def createReview(request,pk):
    usernameg = None
    if request.user.is_authenticated:
        usernameg = request.user.get_username()

    userinstance =User.objects.get(username=usernameg)
    foodmodelinstance = FoodModel.objects.get(id=pk)
    if request.method =='POST':
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rate']
            text = form.cleaned_data['text']
            obj = ReviewModel(student=userinstance,foodmodel=foodmodelinstance,rate=rate,text=text)
            obj.save()
            return redirect('home')


    form = CreateReviewForm()
    context={
        'form':form,
        'objid' : pk
    }
    return render(request,'FoodApp/create_review.html',context)

def LogOut(request):
    logout(request)
    return redirect('home')


def LogIn(request):
    form = AuthenticationForm
    if request.method == 'POST':
        print('I am in post')
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')

    context= {
        'form':form
    }
    return render(request,'FoodApp/login.html',context)

def register(request):
    form = UserCreationForm
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('login')
    context = {
        "form" : form
    }
    return render(request,'FoodApp/register.html',context)

@login_required(login_url="login")
def AllReviews(request):
    objs = ReviewModel.objects.all()
    context={
        'objs' : objs
    }
    return render(request,'FoodApp/allreviews.html',context)
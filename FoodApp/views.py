from django.shortcuts import render
from FoodApp.models import FoodModel,ReviewModel
import datetime

# Create your views here.
def Home(request):

    today = datetime.date.today()
    itemlist = FoodModel.objects.filter(createdon__year=today.year, createdon__month=today.month, createdon__day=today.day)
    context = {
        "itemlist" : itemlist
    }
    return render(request,'FoodApp/home.html',context)
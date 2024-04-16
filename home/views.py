from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactForm, ContactMessage,FAQ,Slider,Offer
from product.models import Category


def index(request):

    setting = Setting.objects.all().order_by('-id')[:1]
    category = Category.objects.all()    
    context={
        'setting':setting,
        'category':category
    } 
    
    return render(request,'main/index.html',context)

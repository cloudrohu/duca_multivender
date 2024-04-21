from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactForm, ContactMessage,FAQ,Slider,Offer,Banner,Slide_Content
from product.models import Main_Category,Product,Brand


def index(request):

    setting = Setting.objects.all().order_by('-id')[:1]
    content = Slide_Content.objects.all().order_by('-id')[:1]
    slider = Slider.objects.filter(featured_project= 'True').order_by('-id')[:6]
    offer = Offer.objects.filter(featured_project= 'True').order_by('-id')[:6]
    brand = Brand.objects.filter(featured_brand= 'True').order_by('-id')[:6]
    
    banner = Banner.objects.filter(featured_project= 'True').order_by('-id')[:3]
    banner2 = Banner.objects.filter(featured_project= 'True').order_by('-id')[3:5]
    Recommended = Product.objects.filter(Recommended_For_You= 'True').order_by('-id')
    Top_Deals_Of_The_Day = Product.objects.filter(Top_Deals_Of_The_Day= 'True').order_by('-id')
    featured_project_1 = Product.objects.filter(featured_project= 'True').order_by('-id')[0:1]
    featured_project_4 = Product.objects.filter(featured_project= 'True').order_by('-id')[2:5]
    main_category = Main_Category.objects.all()  
    context={
        'setting':setting,
        'main_category':main_category,
        'slider':slider,
        'banner':banner,
        'banner2':banner2,
        'content':content,
        'Recommended':Recommended,
        'Top_Deals_Of_The_Day':Top_Deals_Of_The_Day,
        'offer':offer,
        'brand':brand,
        'featured_project_1':featured_project_1,
        'featured_project_4':featured_project_4,
    } 
    
    return render(request,'main/index.html',context)

def ABOUT(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/ABOUT.html',context)

def CONTACT(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/CONTACT.html',context)

def PRODUCT(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/PRODUCT.html',context)

def PRODUCT_DETAILS(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/PRODUCT_DETAILS.html',context)

def BRAND(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/BRAND.html',context)

def FQA(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/FQA.html',context)

def BLOG(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/BLOG.html',context)

def BLOG_DETAILS(request):
    setting = Setting.objects.all().order_by('-id')[:1]

    context={
        'setting':setting,
    }     
    return render(request,'main/BLOG_DETAILS.html',context)


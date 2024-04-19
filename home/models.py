from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.http import request
from django.utils.safestring import mark_safe
# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    nav_color_1 = models.CharField(blank=True,max_length=150)
    nav_color_2 = models.CharField(blank=True,max_length=150)
    nav_color_3 = models.CharField(blank=True,max_length=150)
    footer_color_1 = models.CharField(blank=True,max_length=150)
    footer_color_2 = models.CharField(blank=True,max_length=150)
    logo = models.ImageField(upload_to='logo/')
    image_1 = models.ImageField(upload_to='logo/')
    image_2 = models.ImageField(upload_to='logo/')
    image_3 = models.ImageField(upload_to='logo/')
    image_about = models.ImageField(upload_to='logo/')
    image_product = models.ImageField(upload_to='logo/')
    image_contact = models.ImageField(upload_to='logo/')
    image_blog = models.ImageField(upload_to='logo/')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    whatsapp = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    pinterest = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    google_map = models.CharField(max_length=1500,blank=True,)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=False,max_length=20)
    email= models.EmailField(blank=False,max_length=50)
    subject= models.CharField(blank=False,max_length=50)
    message= models.TextField(blank=False,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : TextInput (attrs={'class': 'input','placeholder':'Name & Surname',} ),
            'subject' : TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }

class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = RichTextUploadingField()
    status=models.CharField(max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Offer(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    image_2=models.ImageField(upload_to='images/')
    image_3=models.ImageField(upload_to='images/')
    image_4=models.ImageField(upload_to='images/')
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    discount_deal = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    link = models.CharField(max_length=50)    
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    discount_deal = models.CharField(max_length=50)
    link = models.CharField(max_length=50)    
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title


class Slide_Content(models.Model):
    color = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    title_1 = models.CharField(max_length=50)
    title_2 = models.CharField(max_length=50)
    title_3 = models.CharField(max_length=50)
    title_4 = models.CharField(max_length=50)     
    featured_project = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def __str__(self):
        return self.title

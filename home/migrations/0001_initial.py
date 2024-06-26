# Generated by Django 5.0.4 on 2024-04-13 05:16

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=255)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('question', models.CharField(max_length=200)),
                ('answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image_2', models.ImageField(blank=True, upload_to='images/')),
                ('image_3', models.ImageField(blank=True, upload_to='images/')),
                ('image_4', models.ImageField(blank=True, upload_to='images/')),
                ('featured_project', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('logo', models.ImageField(blank=True, upload_to='logo/')),
                ('image_1', models.ImageField(blank=True, upload_to='logo/')),
                ('image_2', models.ImageField(blank=True, upload_to='logo/')),
                ('image_3', models.ImageField(blank=True, upload_to='logo/')),
                ('image_about', models.ImageField(blank=True, upload_to='logo/')),
                ('image_product', models.ImageField(blank=True, upload_to='logo/')),
                ('image_contact', models.ImageField(blank=True, upload_to='logo/')),
                ('image_blog', models.ImageField(blank=True, upload_to='logo/')),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('whatsapp', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('smtpserver', models.CharField(blank=True, max_length=50)),
                ('smtpemail', models.CharField(blank=True, max_length=50)),
                ('smtppassword', models.CharField(blank=True, max_length=10)),
                ('smtpport', models.CharField(blank=True, max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('youtube', models.CharField(blank=True, max_length=50)),
                ('pinterest', models.CharField(blank=True, max_length=50)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('google_map', models.CharField(blank=True, max_length=1500)),
                ('references', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_1', models.CharField(max_length=50)),
                ('title_2', models.CharField(max_length=50)),
                ('title_3', models.CharField(max_length=50)),
                ('title_4', models.CharField(max_length=50)),
                ('featured_project', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('discount_deal', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('featured_project', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_arm_style_assembly_back_style_colour_depth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='main_category',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
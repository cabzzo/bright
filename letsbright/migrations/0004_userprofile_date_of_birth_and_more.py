# Generated by Django 4.2.6 on 2023-10-08 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsbright', '0003_design_product_space_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]

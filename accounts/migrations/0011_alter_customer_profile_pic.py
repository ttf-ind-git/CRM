# Generated by Django 3.2.5 on 2021-07-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='User_Profile.png', null=True, upload_to=''),
        ),
    ]

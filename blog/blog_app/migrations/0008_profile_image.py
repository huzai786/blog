# Generated by Django 4.0.2 on 2022-03-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_alter_profile_address_alter_profile_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/df.png', upload_to=''),
        ),
    ]

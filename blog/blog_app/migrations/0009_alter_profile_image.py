# Generated by Django 4.0.2 on 2022-03-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/df.png', null=True, upload_to=''),
        ),
    ]

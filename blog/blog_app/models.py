from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.conf import settings
from PIL import Image

User = get_user_model()


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=60, blank=False)
    content = models.TextField(max_length=100000, null=True)
    updated = models.DateField(auto_now_add=True, null=True)
    date_created = models.DateField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.id})
    
    @property
    def get_profile_url(self):
        id = self.user.profile.id
        return reverse('profile', kwargs={'pk':id})


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    image = models.ImageField(default='default.png', null=True, blank=True)
    phone_no = models.CharField(max_length=40, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


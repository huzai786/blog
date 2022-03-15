from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Profile, User


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)
        print('Profile created hurray!')


post_save.connect(create_profile, sender=User)
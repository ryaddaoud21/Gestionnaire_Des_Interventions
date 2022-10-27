from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.UserProfile.save()


@receiver(post_save, sender=Intervention)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(Nom_Client=instance.Nom_Client,Numéro=instance.Numéro,Ville=instance.Ville,Address=instance.Address,Code_postal=instance.Code_postal)



@receiver(post_save, sender=Intervention)
def save_profile(sender, instance, **kwargs):
    instance.Client.save()


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Farmer

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Farmer)
def generate_framer_qr(sender, instance, created, **kwargs):
    if created and not instance.qr_code:
        instance.generate_qr_code()
        instance.save()

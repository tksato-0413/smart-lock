from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CreateKey

@receiver(post_save, sender=User)
def create_user_key(sender, instance, created, **kwargs):
    if created:
        CreateKey.objects.create(user=instance)

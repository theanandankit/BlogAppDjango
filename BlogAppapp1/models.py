from django.db import models
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User_info(models.Model):
    user_id=models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name="user_details")
    description=models.CharField(max_length=100)
    url=models.CharField(max_length=150)

    def __str__(self):
        return self.description

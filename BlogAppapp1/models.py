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
    user_id=models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name="user_details",unique=True)
    description=models.CharField(max_length=100, default='Hello There', null=True, blank=True)
    url=models.CharField(max_length=500, null= True, blank=True)

    def __str__(self):
        return self.description


class Following_info(models.Model):
    who=models.ForeignKey(User,to_field='id',on_delete=models.CASCADE, related_name='person_list1')
    whom=models.ForeignKey(User,to_field='id',on_delete=models.CASCADE, related_name='person_list2')

class Groups(models.Model):
    group_id=models.CharField(max_length=10, unique=True)
    group_description=models.CharField(max_length=100)
    url = models.CharField(max_length=200,default="NA")
    creator_id=models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name="creator_details")
    group_code=models.CharField(max_length=6)
    date = models.DateTimeField(auto_now_add=True)

class Blog_info(models.Model):
    url=models.CharField(max_length=500)
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=2000)
    date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='public')
    author=models.ForeignKey(User,to_field='id',on_delete=models.CASCADE, related_name='author_name')
    group = models.ForeignKey(Groups,to_field='group_id',on_delete=models.CASCADE,related_name='groups')

class GroupMembers(models.Model):
    group_id = models.ForeignKey(Groups, to_field='group_id', on_delete=models.CASCADE, related_name="members")
    member_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name="member_info")

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name
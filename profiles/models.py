from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(
        upload_to='images/', default='../avatardefault_xjafxo'
    )
    location = models.CharField(max_length=200, blank=True)
    about_me = models.TextField(blank=True)
    interests = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

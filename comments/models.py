from django.db import models
from django.contrib.auth.models import User
from adventures.models import Adventure


class Comment(models.Model):
    """
    Comment model, related to User and Adventure,
    to provide fields for user's comment content.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    response = models.TextField()
    response_image = models.ImageField(
        upload_to='images/',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.response

from django.db import models
from django.contrib.auth.models import User
from adventures.models import Adventure


class Favourite(models.Model):
    """
    Favourite model, related to User and Adventure,
    to provide user the ability to save Adventure posts.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    adventure_post = models.ForeignKey(
        Adventure, related_name='favourited', on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'adventure_post']
    
    def __str__(self):
        return self.response

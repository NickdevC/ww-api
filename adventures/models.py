from django.db import models
from django.contrib.auth.models import User


class Adventure(models.Model):
    """
    Adventure model, related to 'owner', i.e. a User instance.
    Default image set.
    """
    family_friendly_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unsure', 'Unsure'),
    ]
    all_weather_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unsure', 'Unsure'),
    ]
    terrain_challenge_choices = [
        ('smooth sailing', 'Smooth sailing'),
        ('a little bumpy', 'A little bumpy'),
        ('climbing required', 'Climbing required'),
        ('a real challenge', 'A real challenge!'),
    ]
    cost_choices = [
        ('free', 'Free'),
        ('£', '£'),
        ('££', '££'),
        ('£££', '£££'),
    ]
    duration_choices = [
        ('< 1 hour', '< 1 hour'),
        ('a few hours', 'A few hours'),
        ('half-day', 'Half-day'),
        ('full-day', 'Full-day'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    subheading = models.CharField(max_length=300)
    location = models.CharField(max_length=250)
    post_image = models.ImageField(
        upload_to='images/',
        default='../adventure_default_xreot1',
        blank=True
    )
    family_friendly = models.CharField(
        max_length=8,
        choices=family_friendly_choices,
        default='none'
    )
    all_weather = models.CharField(
        max_length=8,
        choices=all_weather_choices,
        default='none'
    )
    terrain_challenge = models.CharField(
        max_length=30,
        choices=terrain_challenge_choices,
        default='none'
    )
    cost = models.CharField(
        max_length=8,
        choices=cost_choices,
        default='none'
    )
    duration = models.CharField(
        max_length=20,
        choices=duration_choices,
        default='none'
    )
    description = models.TextField(blank=True)

    class Meta:
        """Order adventures by most recent first"""
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.id} {self.title}'

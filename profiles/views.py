from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from ww_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by Django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        adventures_count=Count('owner__adventure', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'adventures_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if user is the owner.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        adventures_count=Count('owner__adventure', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    # queryset = Profile.objects.all()

from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from ww_api.permissions import IsOwnerOrReadOnly
from .models import Adventure
from .serializers import AdventureSerializer


class AdventureList(generics.ListCreateAPIView):
    """
    List adventure posts or create adventure posts if
    logged in.
    Perform_create: associates the post with the logged in
    user.
    """
    serializer_class = AdventureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adventure.objects.annotate(
        favourites_count=Count('favourited', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'favourited__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'family_friendly',
        'all_weather',
        'cost',
    ]
    ordering_fields = [
        'favourites_count',
        'comments_count',
        'favourited__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdventureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves specific adventure posts, allowing users to edit
    and delete data of the posts they own.
    """
    serializer_class = AdventureSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Adventure.objects.annotate(
        favourites_count=Count('favourited', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')

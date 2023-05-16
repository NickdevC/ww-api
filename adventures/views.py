from rest_framework import generics, permissions
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
    queryset = Adventure.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdventureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves specific adventure posts, allowing users to edit
    and delete data of the posts they own.
    """
    serializer_class = AdventureSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Adventure.objects.all()

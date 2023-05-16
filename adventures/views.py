# from django.http import Http404
# from rest_framework import status, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Adventure
# from .serializers import AdventureSerializer
# from ww_api.permissions import IsOwnerOrReadOnly
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

# class AdventureList(APIView):
#     """List all adventure posts"""
#     serializer_class = AdventureSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly
#     ]

#     def get(self, request):
#         adventures = Adventure.objects.all()
#         serializer = AdventureSerializer(
#             adventures, many=True, context={'request': request}
#         )
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = AdventureSerializer(
#             data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )


class AdventureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves specific adventure posts, allowing users to edit
    and delete data of the posts they own.
    """
    serializer_class = AdventureSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Adventure.objects.all()

# class AdventureDetail(APIView):
#     """
#     Retrieves specific adventure post details, allowing users
#     to edit and delete the post's information.
#     """
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = AdventureSerializer

#     def get_object(self, pk):
#         try:
#             adventure = Adventure.objects.get(pk=pk)
#             self.check_object_permissions(self.request, adventure)
#             return adventure
#         except Adventure.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         adventure = self.get_object(pk)
#         serializer = AdventureSerializer(
#             adventure, context={'request': request}
#         )
#         return Response(serializer.data)

#     def put(self, request, pk):
#         adventure = self.get_object(pk)
#         serializer = AdventureSerializer(
#             adventure, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )
    
#     def delete(self, request, pk):
#         adventure = self.get_object(pk)
#         adventure.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

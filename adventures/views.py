from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Adventure
from .serializers import AdventureSerializer


class AdventureList(APIView):
    serializer_class = AdventureSerializer

    def get(self, request):
        adventures = Adventure.objects.all()
        serializer = AdventureSerializer(
            adventures, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def adventure(self, request):
        serializer = AdventureSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Adventure
from .serializers import AdventureSerializer


class AdventureList(APIView):
    def get(self, request):
        adventures = Adventure.objects.all()
        serializer = AdventureSerializer(
            adventures, many=True, context={'request': request}
        )
        return Response(serializer.data)

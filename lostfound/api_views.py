from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateAPI(generics.ListCreateAPIView):
   queryset = Item.objects.all().order_by('-created_at')
   serializer_class = ItemSerializer

class ItemDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer

class UserProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

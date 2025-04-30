from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Herb
from .serializers import HerbSerializer
# Create your views here.
class  HerbListCreateView(APIView):
    def get(self, request):
        herbs = Herb.objects.all() 
        serializer = HerbSerializer(herbs, many=True) 
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = HerbSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class HerbDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Herb, pk=pk)
    
    def get(self, request, pk):
        herb = self.get_object(pk)
        serializer = HerbSerializer(herb)
        return Response(serializer.data)
from django.shortcuts import render
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
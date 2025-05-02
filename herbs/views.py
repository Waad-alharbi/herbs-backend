from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Herb, Category, HealthTracker
from .serializers import HerbSerializer, CategorySerializer, HealthTrackerSerializer
from rest_framework import generics
# Create your views here.

#https://www.django-rest-framework.org/api-guide/generic-views/
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
    
    def delete(self, request, pk):
        herb = self.get_object(pk)
        herb.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        herb = self.get_object(pk)
        serializer = HerbSerializer(herb, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class HealthTrackerListCreateView(APIView):
    def get(self, request):
        logs = HealthTracker.objects.all()
        serializer = HealthTrackerSerializer(logs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HealthTrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class HealthlogDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(HealthTracker, pk=pk)
    
    def get(self, request, pk):
        log = self.get_object(pk)
        serializer = HealthTrackerSerializer(log)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        log = self.get_object(pk)
        log.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        log = self.get_object(pk)
        serializer = HealthTrackerSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    

    
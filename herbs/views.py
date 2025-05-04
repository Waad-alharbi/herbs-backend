from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Herb, Category, HealthTracker
from .serializers import HerbSerializer, CategorySerializer, HealthTrackerSerializer
from rest_framework import generics, permissions, status
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
# Create your views here.

#https://www.django-rest-framework.org/api-guide/generic-views/
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class HerbListAPIView(generics.ListAPIView):
    queryset = Herb.objects.all()
    serializer_class = HerbSerializer

class  HerbListCreateView(APIView):
    def get(self, request):
        herbs = Herb.objects.all() 
        serializer = HerbSerializer(herbs, many=True) 
        return Response(serializer.data, status=200)
    
    def post(self, request):
        if not request.user.is_staff:
            return Response({'only admin can add herb'})
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
        if not request.user.is_staff:
            return Response({'only admin can add herb'})
        herb = self.get_object(pk)
        herb.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        if not request.user.is_staff:
            return Response({'only admin can add herb'})
        herb = self.get_object(pk)
        serializer = HerbSerializer(herb, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class HealthTrackerListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        logs = HealthTracker.objects.filter(user=request.user)
        serializer = HealthTrackerSerializer(logs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = HealthTrackerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class HealthlogDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(HealthTracker, pk=pk)
    
    def get(self, request, pk):
        log = self.get_object(pk, request.user)
        serializer = HealthTrackerSerializer(log)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        log = self.get_object(pk, request.user)
        log.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        log = self.get_object(pk, request.user)
        serializer = HealthTrackerSerializer(log, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )
    

    
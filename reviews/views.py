from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, \
    ReviwSerializer, BusinessSerializer, CategorySerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Business, Category, Review


# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GroupSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReviwSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BusinessSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer

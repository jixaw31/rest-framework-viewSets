from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'groups', views.GroupViewSet, basename='group')
router.register(r'reviews', views.ReviewViewSet, basename='review')
router.register(r'businesses', views.BusinessViewSet, basename='business')
router.register(r'categories', views.CategoryViewSet, basename='category')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('display/', views.home, name='home'),
]

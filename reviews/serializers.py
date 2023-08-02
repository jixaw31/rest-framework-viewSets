from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User, Group
from .models import Business, Category, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # we could use normal serializer like modelserializer
    # we use url instead of primary key
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # we could use normal serializer like modelserializer
    # we use url instead of primary key
    class Meta:
        model = Group
        fields = ['url', 'name']


class ReviwSerializer(serializers.HyperlinkedModelSerializer):
    # we could use normal serializer like modelserializer
    # we use url instead of primary key
    class Meta:
        model = Review
        fields = ['url', 'title', 'stars', 'content', 'user', 'business']
        #         you could use all and url would be added automatically
        # fields = '__all__'


class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    # we could use normal serializer like modelserializer
    # we use url instead of primary key
    class Meta:
        model = Business
        fields = '__all__'

    validators = [
        UniqueTogetherValidator(
            queryset=Business.objects.all(),
            fields=['phone']
        )
    ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # we could use normal serializer like modelserializer
    # we use url instead of primary key
    class Meta:
        model = Category
        fields = '__all__'

from abc import ABC

from rest_framework import serializers
from .models import Estate


class EstateGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
        write_only_fields = ('id', 'user', 'sold', 'created_at')


class EstateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'


class EstateFilterSerializer(serializers.Serializer):
    score = serializers.ChoiceField(default=0, choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))


class EstateCommentSerializer(serializers.Serializer):
    score = serializers.CharField(default='Your Comment')

from abc import ABC

from rest_framework import serializers
from .models import Estate


class EstateGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
        write_only_fields = ('id', 'user', 'created_at')


class EstateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
        read_only_fields = ('user', 'sold', 'created_at', 'updated_at')


class EstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
        required_fields = ['district', 'area', 'floor', 'rooms', 'construction_year']


class EstateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = ['sold', 'updated_at']

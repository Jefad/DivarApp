from abc import ABC

from rest_framework import serializers
from .models import Estate


class EstateGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
        write_only_fields = ('id', 'user', 'created_at')

    def __init__(self, *args, **kwargs):
        super(EstateGetSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'GET':
            excluded_fields = ['id', 'user', 'created_at']
            for field_name in excluded_fields:
                self.fields.pop(field_name)


class EstateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
        read_only_fields = ('sold', 'created_at', 'updated_at')
        required = ('user', 'title', 'district', 'area', 'floor', 'construction_year', 'price')

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     validated_data['user'] = user
    #     return super().create(validated_data)


class EstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'
        required_fields = ['district', 'area', 'floor', 'rooms', 'construction_year']


class EstateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = ['sold', 'updated_at']

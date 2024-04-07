from rest_framework import generics, status, permissions
from rest_framework.response import Response

from django.contrib import admin

from .models import Estate, State, City, District
from .serializers import EstateGetSerializer, EstateUpdateSerializer, EstateCommentSerializer


class EstateCreateAPIView(generics.CreateAPIView, generics.ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateGetSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = EstateGetSerializer(data=data)

        if serializer.is_valid():
            estate = Estate.objects.create(**serializer.validated_data)
            return Response({'detail': 'The new Estate was created.',
                             'Estate features': serializer.validated_data}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)


class EstateDetailAPIView(generics.RetrieveAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateGetSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        filtered_data = Estate.objects.filter(id=kwargs.get('pk')).values()
        return Response(data=filtered_data.last())


class EstateUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def update(self, request, *args, **kwargs):


class EstateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateGetSerializer
    permission_classes = [permissions.AllowAny]


class StateView(admin.ModelAdmin):
    class Meta:
        model = State
        fields = '__all__'


admin.site.register(Estate, StateView)
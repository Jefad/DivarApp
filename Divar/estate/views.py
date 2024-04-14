from rest_framework import generics, status, permissions
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Estate
from .serializers import EstateGetSerializer, EstateCreateSerializer, EstateListSerializer, EstateUpdateSerializer


class EstateCreateAPIView(generics.CreateAPIView, generics.ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        # requested_user = self.request.user
        # user = authenticate(request, username=requested_user.username, password=requested_user.password)

        access_token = request.headers.get('Authorization')

        if not access_token:
            raise AuthenticationFailed('Access token is required')

        try:
            jwt_authentication = JWTAuthentication()
            user, _ = jwt_authentication.authenticate(request)
            data = self.request.data
            serializer = EstateCreateSerializer(data=data)
        except AuthenticationFailed as e:
            return Response({'detail': 'Unauthorized user.'}, status=401)

        if serializer.is_valid():
            estate = Estate.objects.create(user=self.request.user, **serializer.validated_data)
            return Response({'detail': 'The new Estate was created.'}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)


class EstateDetailAPIView(generics.RetrieveAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateGetSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    lookup_field = 'pk'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def retrieve(self, request, *args, **kwargs):
        try:
            filtered_data = Estate.objects.filter(id=kwargs.get('pk'), sold=False).values()
            return Response(data=filtered_data.last(), status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)


class EstateListView(generics.ListAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateListSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_params = {}
        query_params = self.request.query_params
        for key, value in query_params.items():
            if key in EstateListSerializer.Meta.required_fields:
                filter_params[key] = value
        filter_params['sold'] = False
        return queryset.filter(**filter_params)


class EstateUpdateView(generics.UpdateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateUpdateSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.sold = True
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

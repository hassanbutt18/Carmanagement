from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile
from .serializers import UserProfileSerializer, UserProfileResponseSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileResponseSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            headers = self.get_success_headers(serializer.data)
            result_serializer = self.serializer_class(user).data
            data = {
                "msg":"User created successfully",
                "data":result_serializer
            }
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from WheelWorks.models import Vehicle
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .pagination import CustomPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import VehicleSerializer, VehicleSerializerResponse


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializerResponse
    pagination_class = CustomPagination
    permission_class = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                serializer = VehicleSerializer(data=request.data,context={"owner":request.user})
                if serializer.is_valid():
                    vehicle = serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    result_serializer = self.serializer_class(vehicle).data
                    data = {
                        "msg": "Vehicle created successfully",
                        "data": result_serializer
                    }
                    return Response(data, status=status.HTTP_201_CREATED, headers=headers)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"msg":"You are not authorized to perform this action"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({"msg": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            # Retrieve the instance of Vehicle
            instance = get_object_or_404(Vehicle, id=self.kwargs.get('pk'))
            if instance.owner == request.user:
                serializer = VehicleSerializer(instance, data=request.data, partial=True)
                if serializer.is_valid():
                    vehicle = serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    result_serializer = self.serializer_class(vehicle).data
                    data = {
                        "msg": "Vehicle updated successfully",
                        "data": result_serializer
                    }
                    return Response(data, status=status.HTTP_200_OK, headers=headers)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"msg":"You are not authorized to perform this action"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"msg": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            # Retrieve the instance of Vehicle
            vehicle_instance = Vehicle.objects.filter(id=self.kwargs.get('pk'))
            if vehicle_instance:
                instance = vehicle_instance.first()
                if instance.owner == request.user:
                    vehicle_instance.delete()
                    return Response({"msg":"Successfully delete the Vehicle"}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "Vehicle does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"msg": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST)



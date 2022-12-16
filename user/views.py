from rest_framework.generics import CreateAPIView, RetrieveAPIView

from user.serializers import (
    GenerateClientSerializer,
    AddUserSerializer,
    ListClientSerializer,
)


class GenerateConfig(CreateAPIView):
    serializer_class = GenerateClientSerializer


class AddUser(CreateAPIView):
    serializer_class = AddUserSerializer


class ListUsers(RetrieveAPIView):
    serializer_class = ListClientSerializer

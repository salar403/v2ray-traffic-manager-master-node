from rest_framework import serializers
from backend.customs.exceptions import CustomException
from backend.customs.paginator import custom_paginator

from backend.services.config_generator import generate_config
from backend.services.user_config_manager import assign_client

from user.models import V2rayClient, User


class GenerateClientSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(required=True, min_value=1, max_value=1000)

    def create(self, validated_data):
        generate_config(quantity=validated_data["quantity"])
        total_clients = V2rayClient.objects.count()
        self._data = {"code": "success", "total_clients": total_clients}
        return True


class ClientSerializer(serializers.ModelField):
    class Meta:
        model = V2rayClient
        fields = ["uuid", "name", "limited"]

    def to_representation(self, obj):
        ret = super().to_representation(obj)
        user_info = UserSerializer(obj.user).data
        return {**ret, **user_info}


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"


class AddUserSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        user, created = User.objects.get_or_create(
            telegram_id=validated_data["telegram_id"]
        )
        if not created:
            raise CustomException(code="duplicated_user")
        config = assign_client(user=user)
        self._data = {"code": "success", "data": ClientSerializer(config).data}
        return True


class ListClientSerializer(serializers.Serializer):
    page = serializers.IntegerField(default=1, min_value=1)
    per_page = serializers.IntegerField(default=10, max_value=100)
    telegram_id = serializers.IntegerField(rquired=False, min_value=1)
    uuid = serializers.CharField(required=False)
    cdn = serializers.IntegerField(min_value=1, max_value=2, required=False)

    def validate(self, attrs):
        self.filters = {}
        if "telegram_id" in attrs:
            self.filters["user__telegram_id"] = attrs["telegram_id"]
        if "uuid" in attrs:
            self.filters["uuid"] = attrs["uuid"]
        if "cdn" in attrs:
            self.filters["cdn"] = attrs["cdn"]
        return super().validate(attrs)

    def to_representation(self, instance):
        super().to_representation(instance)
        queryset = V2rayClient.objects.filter(**self.filters)
        page = instance["page"]
        per_page = instance["per_page"]
        total = queryset.count()
        data = ClientSerializer(
            custom_paginator(queryset, {"page": page, "per_page": per_page}),
            many=True,
        ).data
        return {
            "success": True,
            "data": data,
            "page": page,
            "per_page": per_page,
            "total": total,
        }

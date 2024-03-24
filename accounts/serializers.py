from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        email = attrs.get('email', None)
        if email is None:
            raise serializers.ValidationError({"msg": "Enter a valid email address"})
        return attrs

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'address', 'country', 'language',
                  ]

    def create(self, validated_data):
        user_profile = UserProfile.objects.create(first_name=validated_data.get('first_name', None),
                                                  last_name=validated_data.get('last_name', None),
                                                  email=validated_data.get('email', None),
                                                  username=validated_data.get('email', None),
                                                  date_of_birth=validated_data.get('date_of_birth', None),
                                                  gender=validated_data.get('gender', None),
                                                  address=validated_data.get('address', None),
                                                  country=validated_data.get('country', None),
                                                  language=validated_data.get('language', None),
                                                  )
        return user_profile


class UserProfileResponseSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()

    def get_access_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        access_token = str(refresh.access_token)
        return access_token

    def get_refresh_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return str(refresh)

    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'address', 'country', 'language',
                  'access_token', 'refresh_token']




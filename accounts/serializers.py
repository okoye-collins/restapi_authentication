from rest_framework import serializers


from .utils import send_otp_code
from .models import OneTimePassword, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password", "")
        password2 = attrs.get("password2", "")

        if password != password2:
            raise serializers.ValidationError("passwords do not match")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )
        send_otp_code(user.email)
        return user


class VerifyUserEmailSerializer(serializers.ModelSerializer):
    # opt = serializers.CharField(max_length=6)
    
    class Meta:
        model = OneTimePassword
        fields = ["code"]

    def validate(self, attrs):
        otp_code = attrs.get("opt")

        try:
            user_code_obj = OneTimePassword.objects.get(code=otp_code)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
            raise serializers.ValidationError("code is not valid")
        except OneTimePassword.DoesNotExist:
            raise serializers.ValidationError("passcode not provided")

        return super().validate(attrs)

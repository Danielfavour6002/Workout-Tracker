from .models import User, Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
    write_only=True,      
    required=True
    ) 
    class Meta:
        model = User
        fields = ("id", "username", "password", "confirm_password", "first_name", "last_name", "email")
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, data):
        """Ensure both passwords match."""
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    bmi = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ("user", "bio", "weight", "height", "age", "bmi")
        read_only_fields = ["user"]

    def get_bmi(self, obj):
        if not obj.height:  # avoid division by zero
            return None
        height_m = obj.height / 100  # convert cm → meters if height stored in cm
        bmi = obj.weight / (height_m ** 2)
        return round(bmi, 2)

class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    class Meta:
        model = Profile
        fields = ("first_name", "last_name","username", "email", "bio", "weight", "height", "age")



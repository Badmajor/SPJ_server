from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.HiddenField(default=False)
    is_staff = serializers.HiddenField(default=False)
    user_permissions = serializers.HiddenField(default=[])
    class Meta:
        fields = '__all__'
        model = User
        read_only_field = (
            'id',
            'date_joined',
            'is_staff',
            'is_superuser',
            'last_login',
        )
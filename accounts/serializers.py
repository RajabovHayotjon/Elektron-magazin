from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Kerakli maydonlarni aniq belgilash
        fields = ['id', 'phone_number', 'email', 'is_active']  # Misol uchun kerakli maydonlar
        extra_kwargs = {
            'password': {'write_only': True},  # Parolni faqat yozish uchun
        }

    # Parolni yaratishda xato chiqmasligi uchun custom create funksiyasi
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

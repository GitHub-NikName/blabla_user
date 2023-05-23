from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.core.validators import FileExtensionValidator

from user.models import Audio


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    """Сериализация создания пользователя"""

    username = serializers.CharField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'uuid')
        read_only_fields = ('id', 'uuid')


class RecordSerializer(serializers.ModelSerializer):
    """Аудиозаписи"""

    user = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)
    url = serializers.SerializerMethodField()
    file = serializers.FileField(
        write_only=True,
        validators=[FileExtensionValidator(allowed_extensions=['wav'])],
    )

    class Meta:
        model = Audio
        exclude = ('id', 'uuid')

    def validate(self, attrs):
        if not User.objects.filter(id=attrs['user'], uuid=attrs['token']):
            raise serializers.ValidationError('Неправильный id пользователя '
                                              'или токен')
        return attrs

    def create(self, validated_data):
        validated_data.pop('token')
        return Audio.objects.create(**validated_data)

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(
            '../record?id=%s&user=%s' % (obj.id, obj.user.id))

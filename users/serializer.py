from rest_framework.serializers import ModelSerializer

from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'mail', 'age', 'first_name', 'last_name')


class UserModelSerializerAll(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

from rest_framework import serializers
from Ewall.models import UserText

from django.contrib.auth.models import User


class UserTextSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserText
        fields = ('id', 'text', 'owner')


class UserSerializer(serializers.ModelSerializer):

    texts = serializers.PrimaryKeyRelatedField(many=True, queryset=UserText.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'texts')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
        )
        return user





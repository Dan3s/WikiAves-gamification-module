from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create (self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])#Para encriptar la contraseña
        user.save()
        return user

    def update (self, instance, validate_data):
        update_user = super().update(instance, validate_data) #Para que haga su atualización automatica
        update_user.set_password(validate_data['password']) #Para que se encripte la contraseña cuando se guarde
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': instance['name'],
            'last_names': instance['last_names'],
            'username': instance['username'],
            'password': instance['password'],
            'email': instance['email'],
            'city': instance['city'],
            'region': instance['region']
        }
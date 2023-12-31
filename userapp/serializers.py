from rest_framework import serializers
from .models import UserData
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Include the email in the token's payload
        token['email'] = user.email

        return token 


class UserDataSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields =' __all__'



# class AdvocateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Advocate
#         fields = ['extra_values']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserData
#         fields = ["id", "email", "name", "password"]
#     def create(self, validated_data):
#         user = UserData.objects.create(email=validated_data['email'], name=validated_data['name'])
#         user.set_password(validated_data['password'])
#         user.save()
#         related = Advocate.objects.create(user=user,age=10,phone='7994626352',enrollment_id='IDSAMPLE',
#                                           specialization='sample')
#         related.save()
#         return user
    
# class UserOnlySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserData
#         fields = ["id", "email", "name", "password","type_of_user"]
#     def create(self, validated_data):
#         user = UserData.objects.create(email=validated_data['email'],
#                                        name=validated_data['name'],type_of_user=validated_data['type_of_user']
#                                          )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    

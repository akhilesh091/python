from rest_framework import serializers
from userapp.models import Registrar, UserData
from advocates.serializer import UserSerializer
from association.models import Court
from association.serializer import CourtListSerializer

class RegistrarSerializer(serializers.ModelSerializer):
    court=CourtListSerializer(read_only=True)
    court_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Court.objects.all(), source='court')   
    user = UserSerializer(read_only=True) 
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserData.objects.all(), source='user')   

    class Meta:
        model = Registrar
        fields = "__all__"

class RegistrarGetSerializer(serializers.ModelSerializer):
    court=CourtListSerializer()
    user = UserSerializer()

    class Meta:
        model = Registrar
        fields = "__all__"
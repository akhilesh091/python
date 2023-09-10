from rest_framework import serializers
from userapp.models import UserData, Advocate
from userapp.serializers import UserDataSerilizer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"

class NormalAdvocateSerializer(serializers.ModelSerializer):
    user = UserDataSerilizer(read_only=True) 
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserData.objects.all(), source="user")
    class Meta:
        model = Advocate
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('type_of_user') == 'normal_advocate':
            return data
        return None
from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    isim = serializers.CharField()
    email = serializers.EmailField()
    tel_numara = serializers.CharField()
    kayit_tarihi = serializers.DateTimeField()
    aktif = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.isim = validated_data.get('isim', instance.isim)
        instance.email = validated_data.get('email', instance.email)
        instance.tel_numara = validated_data.get('tel_numara', instance.tel_numara)
        instance.kayit_tarihi = validated_data.get('kayit_tarihi', instance.kayit_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance
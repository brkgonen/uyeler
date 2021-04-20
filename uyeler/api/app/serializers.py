from rest_framework import serializers
from api.models import User

from datetime import datetime, timezone
from django.utils.timesince import timesince



class UserSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    class Meta:
        model =  User
        fields = '__all__'

    def get_time_since_pub(self, object):
        now = datetime.now(timezone.utc)
        pub_date = object.kayit_tarihi
        time_delta = timesince(pub_date,now)
        return time_delta


####Standart
class UserDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    isim = serializers.CharField()
    email = serializers.EmailField()
    tel_numara = serializers.CharField()
    kayit_tarihi = serializers.DateTimeField(read_only=True)
    aktif = serializers.BooleanField()

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
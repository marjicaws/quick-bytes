from rest_framework import serializers
from quickbytes.models import Byte


class ByteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Byte
        fields = '__all__'

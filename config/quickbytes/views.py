from rest_framework import viewsets
from quickbytes.serializers import ByteSerializer
from quickbytes.models import Byte


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Byte.objects.all()
    serializer_class = ByteSerializer

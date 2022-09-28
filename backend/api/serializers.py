from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=20)

    class Meta:
        model = Contact
        fields = ('__all__')
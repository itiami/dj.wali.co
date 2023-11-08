from rest_framework import serializers
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'homeNo', 'street', 'postCode', 'city', 'country')
        # fields = '__all__'

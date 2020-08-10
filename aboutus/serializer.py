from rest_framework import serializers
from .models import AboutUs


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'source', 'pickUpFrom', 'deliveryTo', 'yourName', 'emailId',
                  'phoneNo', 'truckType', 'dateTime', 'ord_status']
        # fields = '__all__'
        # def to_representation(self, instance):
        #     representation = super(AboutSerializer, self).to_representation(instance)
        #     representation['dateTime'] = instance.created_at.strftime("%m/%d/%Y%H:%M:%S")
        #     return representation

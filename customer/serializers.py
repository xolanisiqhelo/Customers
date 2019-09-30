from rest_framework import serializers
from customer.models import *


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['taskID', 'customerCode', 'custFirstName', 'custLastname', 'deliveryaddress', 'statusCode',
                  'statusDescription']


class CodeReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeReference
        fields = ['statusCode', 'description']


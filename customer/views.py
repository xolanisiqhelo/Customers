from customer.serializers import CustomersSerializer, CodeReferenceSerializer
from rest_framework import generics
from .models import *


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer


class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer


class CodeReferenceList(generics.ListCreateAPIView):
    queryset = CodeReference.objects.all()
    serializer_class = CodeReferenceSerializer


class CodeReferenceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodeReference.objects.all()
    serializer_class = CodeReferenceSerializer
    y = ['100', '200', '300', '400']
    for x in y:
        s = CodeReference.objects.filter(statusCode=str(x))
        #print(s)

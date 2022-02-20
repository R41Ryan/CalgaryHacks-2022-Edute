from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import AccountSerializer, DriverSerializer, ReportSerializer, PostingPassengerSerializer, PostingSerializer
from .models import Account, Driver, Report, Posting, PostingPassenger
from api import serializers

class AccountView (APIView):
    def get(self, request, format=None):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = AccountSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail (APIView):
    def get(self, request, id, format=None):
        account = Account.objects.get (idSchool=id)
        serializer = AccountSerializer(account)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        account = Account.objects.filter(idSchool=id).first()
        serializer = AccountSerializer(account, data=request.data)
        print(account)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        account = Account.objects.filter (idSchool=id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
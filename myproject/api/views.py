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
    def get(self, request, name, format=None):
        account = Account.objects.get (school=name, many=True)
        serializer = AccountSerializer(account)
        return Response (serializer.data)

    def delete(self, request, name, format=None):
        account = Account.objects.filter (school=name)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountDetailBeta(APIView):
    def get(self, request, name, id, format=None):
        account = Account.objects.get(school=name)
        account2 = account.filter(idSchool=id).first()
        serializer = Account(account2)
        return Response(serializer.data)

    def put(self, request, name, id, format=None):
        account = Account.objects.filter(postingId=name)
        account2 = account.filter(idPassenger=id).first()
        serializer = AccountSerializer(account2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, id, format=None):
        account = Account.objects.filter(postingId=name)
        account2 = account.filter(idPassenger=id)
        account2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DriverView (APIView):
    def get(self, request, format=None):
        driver = Driver.objects.all()
        serializer = DriverSerializer(driver, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = DriverSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverDetail (APIView):
    def get(self, request, id, format=None):
        driver = Driver.objects.get (idSchool=id)
        serializer = DriverSerializer(driver)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        driver = Driver.objects.filter(idSchool=id).first()
        serializer = DriverSerializer(driver, data=request.data)
        print(driver)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        driver = Driver.objects.filter (idSchool=id)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostingView (APIView):
    def get(self, request, format=None):
        posting = Posting.objects.all()
        serializer = PostingSerializer(posting, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = PostingSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostingDetail (APIView):
    def get(self, request, id, format=None):
        posting = Posting.objects.get (postingId=id)
        serializer = PostingSerializer(posting)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        posting = Posting.objects.filter(postingId=id).first()
        serializer = PostingSerializer(posting, data=request.data)
        print(posting)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        posting = Posting.objects.filter (postingId=id)
        posting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReportDetail (APIView):
    def get(self, request, id, format=None):
        report = Report.objects.get (idSchool=id)
        serializer = ReportSerializer(report)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        report = Report.objects.filter(idSchool=id).first()
        serializer = ReportSerializer(report, data=request.data)
        print(report)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        report = Report.objects.filter (idSchool=id)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReportView (APIView):
    def get(self, request, format=None):
        report = Report.objects.all()
        serializer = ReportSerializer(report, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = ReportSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostingPassengerView(APIView):
    def get(self, request, format=None):
        postingPassenger = PostingPassenger.objects.all()
        serializer = PostingPassengerSerializer(postingPassenger, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostingPassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostingPassengerDetail(APIView):
    def get(self, request, num, format=None):
        postingPassenger = PostingPassenger.objects.filter(postingId=num)
        serializer = PostingPassengerSerializer(postingPassenger, many=True)
        return Response(serializer.data)

    def delete(self, request, num, format=None):
        postingPassenger = PostingPassenger.objects.filter(postingId=num)
        postingPassenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostingPassengerDetailBeta(APIView):
    def put(self, request, num, id, format=None):
        postingPassenger = PostingPassenger.objects.filter(postingId=num)
        postingPassenger2 = postingPassenger.filter(idPassenger=id).first()
        serializer = PostingPassengerSerializer(postingPassenger2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, id, format=None):
        postingPassenger = PostingPassenger.objects.filter(postingId=num)
        postingPassenger2 = postingPassenger.filter(idPassenger=id)
        postingPassenger2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
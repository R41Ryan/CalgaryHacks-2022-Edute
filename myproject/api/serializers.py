from django.db.models import fields
from rest_framework import serializers
from . import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        field = "__all__"

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        field = "__all__"

class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Posting
        field = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        field = "__all__"

class PostingPassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostingPassenger
        field = "__all__"
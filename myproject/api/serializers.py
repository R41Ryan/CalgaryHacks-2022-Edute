from django.db.models import fields
from rest_framework import serializers
from . import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = "__all__"

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = "__all__"

class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Posting
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = "__all__"

class PostingPassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostingPassenger
        fields = "__all__"
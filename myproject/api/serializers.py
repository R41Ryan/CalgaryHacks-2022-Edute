from django.db.models import fields
from rest_framework import serializers
from . import models

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'

class PharmaceuticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pharmaceutical
        fields = '__all__'

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drug
        fields = '__all__'

class VitaminHerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VitaminHerb
        fields = '__all__'

class MedicineCaseContainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicineCaseContains
        fields = '__all__'

class MedicalUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalUnit
        fields = '__all__'

class MedicalBedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalBed
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Supplier
        fields = "__all__"

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery
        fields = "__all__"

class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Supplies
        fields = "__all__"

class SupplierLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SupplierLocation
        fields = "__all__"

class DeliveryContainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryContains
        fields = "__all__"

class CarriedOutBySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarriedOutBy
        fields = "__all__"

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Diagnosis
        fields = "__all__"

class NurseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NurseOrder
        fields = "__all__"
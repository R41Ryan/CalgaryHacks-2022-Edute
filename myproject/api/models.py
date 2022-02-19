from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from sklearn.metrics import pair_confusion_matrix


# Create your models here.

class Account(models.Model):
    idSchool = models.IntegerField(primary_key=True)
    phoneNum = models.IntegerField()
    image = models.ImageField(upload_to='studentImages')

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.idSchool)

class Driver(models.Model):
    idSchool = models.ForeignKey(Account, on_delete=CASCADE, related_name='driverAccountId')
    licenseNum = models.IntegerField()
    insurancePolicyNum = models.IntegerField()
    driverHistoryFilePath = models.FileField(upload_to="driverHistory")

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.idSchool)

class Posting(models.Model):
    postingId = models.IntegerField(primary_key=True)
    

"""
class Staff(models.Model):
    employeeID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    employeeType = models.CharField(max_length=255)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.employeeID)

class Patient(models.Model):
    healthcareNum = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    primaryNurseId = models.ForeignKey(Staff, null=True, on_delete=SET_NULL, related_name='primaryNurse')
    secondaryNurseId = models.ForeignKey(Staff, null=True, on_delete=SET_NULL, related_name='secondaryNurse')

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.healthcareNum)

class Pharmaceutical(models.Model):
    name = models.CharField(max_length=255)
    numberInStock = models.IntegerField()
    IdPharmaceutical = models.IntegerField(max_length=255, primary_key=True)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.IdPharmaceutical)

class Drug(models.Model):
    DIN = models.IntegerField()
    IdPharmaceutical = models.OneToOneField(Pharmaceutical, on_delete=CASCADE, primary_key=True)
    
    class Meta:
        app_label='api'
    
    def __str__(self):
        return str(self.DIN)

class VitaminHerb(models.Model):
    VIN = models.IntegerField()
    IdPharmaceutical = models.OneToOneField(Pharmaceutical, on_delete=CASCADE, primary_key=True)
    
    class Meta:
        app_label='api'
    
    def __str__(self):
        return str(self.VIN)

class MedicineCaseContains(models.Model):
    patientHealthcareNum = models.ForeignKey(Patient, on_delete=CASCADE, related_name='medCasePatient')
    IdPharmaceutical = models.ForeignKey(Pharmaceutical, on_delete=CASCADE, related_name='medCasePharmaceutical')
    numberOfPharmaceutical = models.IntegerField()
    
    class Meta:
        app_label='api'
        unique_together = ('patientHealthcareNum', 'IdPharmaceutical')

class MedicalUnit(models.Model):
    Number = models.IntegerField(primary_key=True)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.Number)

class MedicalBed(models.Model):
    Number = models.IntegerField()
    medUnitNumber = models.ForeignKey(MedicalUnit, on_delete=CASCADE, related_name='medicalUnit')
    occupyingPatientNum = models.ForeignKey(Patient, null=True, on_delete=SET_NULL, related_name='bedPatient')

    class Meta:
        app_label='api'
        unique_together = ('Number', 'medUnitNumber')

class Supplier(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.name

class Delivery(models.Model):
    number = models.AutoField(primary_key=True)
    dateTime = models.DateTimeField(auto_now=True)
    type = models.IntegerField()
    medCase = models.ForeignKey(Patient, null=True, on_delete=CASCADE, related_name='deliveryMedCase')
    supplier = models.ForeignKey(Supplier, null=True, on_delete=CASCADE, related_name='deliverySupplier')

    class Meta:
        app_label='api'

    def __str__(self):
        return self.number

class Supplies(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=CASCADE, related_name='suppliesSupplier')
    delivery = models.ForeignKey(Delivery, on_delete=CASCADE, related_name='suppliesDelivery')

    class Meta:
        app_label='api'
        unique_together = ('supplier', 'delivery')

class SupplierLocation(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=CASCADE)
    location = models.CharField(max_length=255)

    class Meta:
        app_label='api'
        unique_together=('supplier', 'location')

class DeliveryContains(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=CASCADE, related_name='containsDelivery')
    pharmaceutical = models.ForeignKey(Pharmaceutical, on_delete=CASCADE, related_name='containsPharmaceutical')
    numberOfPharmaceutical = models.IntegerField()

    class Meta:
        app_label='api'
        unique_together=('delivery', 'pharmaceutical')

class CarriedOutBy(models.Model):
    delivery = models.OneToOneField(Delivery, primary_key=True, on_delete=CASCADE, related_name='carriedOutByDelivery')
    pharmacist = models.ForeignKey(Staff, on_delete=CASCADE, related_name='carriedOutByPharmacist')
    
    class Meta:
        app_label='api'

class Diagnosis(models.Model):
    doctor = models.ForeignKey(Staff, on_delete=CASCADE, related_name='diagnosisDoctor')
    patient = models.ForeignKey(Patient, on_delete=CASCADE, related_name='diagnosisPatient')
    pharmaceutical = models.ForeignKey(Pharmaceutical, on_delete=CASCADE, related_name='DiagnosisPharmaceutical')
    numberOfPharmaceutical = models.IntegerField()

    class Meta:
        app_label='api'
        unique_together=('patient', 'pharmaceutical')

class NurseOrder(models.Model):
    nurse = models.ForeignKey(Staff, on_delete=CASCADE, related_name='NurseOrderNurse')
    patient = models.ForeignKey(Patient, on_delete=CASCADE, related_name='NurseOrderPatient')
    pharmaceutical = models.ForeignKey(Pharmaceutical, on_delete=CASCADE, related_name='NurseOrderPharmaceutical')
    numberOfPharmaceutical = models.IntegerField()
    dateTime = models.DateTimeField(auto_now=True)

    class Meta:
        app_label='api'
        unique_together=('patient', 'pharmaceutical')
"""
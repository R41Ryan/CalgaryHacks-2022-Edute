from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import DeliveryContainsSerializer, StaffSerializer, PatientSerializer, PharmaceuticalSerializer, DrugSerializer, VitaminHerbSerializer, MedicineCaseContainsSerializer, MedicalUnitSerializer, MedicalBedSerializer, SupplierSerializer, DeliverySerializer, SuppliesSerializer, SupplierLocationSerializer, DeliveryContainsSerializer, CarriedOutBySerializer, DiagnosisSerializer, NurseOrderSerializer
from .models import Staff, Patient, Pharmaceutical, Drug, VitaminHerb, MedicineCaseContains, MedicalUnit, MedicalBed, Supplier, Delivery, Supplies, SupplierLocation, DeliveryContains, CarriedOutBy, Diagnosis, NurseOrder
from api import serializers

class StaffView (APIView):
    def get(self, request, format=None):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = StaffSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffDetail (APIView):
    def get(self, request, id, format=None):
        staff = Staff.objects.get (employeeID=id)
        serializer = StaffSerializer(staff)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        staff = Staff.objects.filter(employeeID=id).first()
        serializer = StaffSerializer(staff, data=request.data)
        print(staff)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        staff = Staff.objects.filter (employeeID=id)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientView (APIView):
    def get(self, request, format=None):
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = PatientSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail (APIView):
    def get(self, request, num, format=None):
        patient = Patient.objects.get (healthcareNum=num)
        serializer = PatientSerializer(patient)
        return Response (serializer.data)

    def put(self, request, num, format=None):
        patient = Patient.objects.filter(healthcareNum=num).first()
        serializer = PatientSerializer(patient, data=request.data)
        print(patient)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, format=None):
        patient = Patient.objects.filter (healthcareNum=num)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PharmaceuticalView (APIView):
    def get(self, request, format=None):
        pharmaceutical = Pharmaceutical.objects.all()
        serializer = PharmaceuticalSerializer(pharmaceutical, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = PharmaceuticalSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PharmaceuticalDetail (APIView):
    def get(self, request, id, format=None):
        pharmaceutical = Pharmaceutical.objects.get (IdPharmaceutical=id)
        serializer = PharmaceuticalSerializer(pharmaceutical)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        pharmaceutical = Pharmaceutical.objects.filter(IdPharmaceutical=id).first()
        serializer = PharmaceuticalSerializer(pharmaceutical, data=request.data)
        print(pharmaceutical)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        pharmaceutical = Pharmaceutical.objects.filter (IdPharmaceutical=id)
        pharmaceutical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DrugView (APIView):
    def get(self, request, format=None):
        drug = Drug.objects.all()
        serializer = DrugSerializer(drug, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DrugSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DrugDetail (APIView):
    def get(self, request, id, format=None):
        drug = Drug.objects.get (IdPharmaceutical=id)
        serializer = DrugSerializer(drug)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        drug = Drug.objects.filter(IdPharmaceutical=id).first()
        serializer = DrugSerializer(drug, data=request.data)
        print(drug)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        drug = Drug.objects.filter (IdPharmaceutical=id)
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VitaminHerbView (APIView):
    def get(self, request, format=None):
        vitamin_herb = VitaminHerb.objects.all()
        serializer = VitaminHerbSerializer(vitamin_herb, many=True)
        return Response(serializer.data)

    def post(self, request, formay=None):
        serializer = VitaminHerbSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VitaminHerbDetail (APIView):
    def get(self, request, id, format=None):
        vitamin_herb = VitaminHerb.objects.get (IdPharmaceutical=id)
        serializer = VitaminHerbSerializer(vitamin_herb)
        return Response (serializer.data)

    def put(self, request, id, format=None):
        vitamin_herb = VitaminHerb.objects.filter(IdPharmaceutical=id).first()
        serializer = VitaminHerbSerializer(vitamin_herb, data=request.data)
        print(vitamin_herb)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        vitamin_herb = VitaminHerb.objects.filter (IdPharmaceutical=id)
        vitamin_herb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicineCaseView (APIView):
    def get(self, request, format=None):
        medicine_case = MedicineCaseContains.objects.all()
        serializer = MedicineCaseContainsSerializer(medicine_case, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicineCaseContainsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class MedicineCaseDetail (APIView):
    def get(self, request, num, format=None):
        medicine_case = MedicineCaseContains.objects.filter(patientHealthcareNum=num)
        serializer = MedicineCaseContainsSerializer(medicine_case, many=True)
        return Response (serializer.data)

class MedicineCasePatientPharmDetail(APIView):
    def put(self, request, num, id, format=None):
        medicine_case = MedicineCaseContains.objects.filter(patientHealthcareNum=num)
        medicine_case2 = medicine_case.filter(IdPharmaceutical=id).first()
        serializer = MedicineCaseContainsSerializer(medicine_case2, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, id, format=None):
        medicine_case = MedicineCaseContains.objects.filter(patientHealthcareNum=num)
        medicine_case2 = medicine_case.filter(IdPharmaceutical=id).first()
        medicine_case2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicalUnitView(APIView):
    def get(self, request, format=None):
        medical_unit = MedicalUnit.objects.all()
        serializer = MedicalUnitSerializer(medical_unit, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicalUnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class MedicalUnitDetail(APIView):
    def delete(self, request, num, format=None):
        medical_unit = MedicalUnit.objects.filter(number=num).first()
        medical_unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicalBedView(APIView):
    def get(self, request, format=None):
        medical_bed = MedicalBed.objects.all()
        serializer = MedicalBedSerializer(medical_bed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicalBedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class MedicalBedDetail(APIView):
    def get(self, request, unit, format=None):
        medical_bed = MedicalBed.objects.filter(medUnitNumber=unit)
        serializer = MedicalBedSerializer(medical_bed, many=True)
        return Response(serializer.data)

class MedicalBedPair(APIView):
    def put(self, request, unit, number, format=None):
        medical_bed1 = MedicalBed.objects.filter(medUnitNumber=unit)
        medical_bed2 = medical_bed1.filter(Number=number).first()
        serializer = MedicalBedSerializer(medical_bed2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, unit, number, format=None):
        medical_bed1 = MedicalBed.objects.filter(medUnitNumber=unit)
        medical_bed2 = medical_bed1.filter(Number=number).first()
        medical_bed2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SupplierView(APIView):
    def get(self, request, format=None):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class SupplierDetail(APIView):
    def delete(self, request, name, format=None):
        supplier = Supplier.objects.filter(name=name).first()
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeliveryView(APIView):
    def get(self, request, format=None):
        delivery = Delivery.objects.all()
        serializer = DeliverySerializer(delivery, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryDetail(APIView):
    def get(self, request, num, format=None):
        delivery = Delivery.objects.filter(number=num).first()
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)

    def put(self, request, num, format=None):
        delivery = Delivery.objects.filter(number=num).first()
        serializer = DeliverySerializer(delivery, data = request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, format=None):
        delivery = Delivery.objects.filter(number=num).first()
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SuppliesView(APIView):
    def get(self, request, format=None):
        supplies = Supplies.objects.all()
        serializer = SuppliesSerializer(supplies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SuppliesSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuppliesSupplierDetail(APIView):
    def get(self, request, supplier, format=None):
        supplies = Supplies.objects.filter(supplier=supplier)
        serializer = SuppliesSerializer(supplies, many=True)
        return Response(serializer.data)

class SuppliesSupplierDeliveryDetail(APIView):
    def delete(self, request, supplier, num, format=None):
        supplies = Supplies.objects.filter(supplier=supplier)
        supplies2 = supplies.filter(delivery=num)
        supplies2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SupplierLocationView(APIView):
    def get(self, request, format=None):
        location = SupplierLocation.objects.all()
        serializer = SupplierLocationSerializer(location, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SupplierLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierLocationDetail(APIView):
    def get(self, request, sup, format=None):
        location = SupplierLocation.objects.filter(supplier=sup)
        serializer = SupplierLocationSerializer(location, many=True)
        return Response(serializer.data)

class SupplierLocationPair(APIView):
    def put(self, request, sup, loc, format=None):
        supplier = SupplierLocation.objects.filter(supplier=sup)
        location = supplier.filter(location=loc).first()
        serializer = SupplierLocationSerializer(location, data = request.data)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, sup, loc, format=None):
        supplier = SupplierLocation.objects.filter(supplier=sup)
        location = supplier.filter(location=loc)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeliveryContainsView(APIView):
    def get(self, request, format=None):
        contains = DeliveryContains.objects.all()
        serializer = DeliveryContainsSerializer(contains, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeliveryContainsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryContainsDetail(APIView):
    def get(self, request, num, format=None):
        contains = DeliveryContains.objects.filter(delivery=num)
        serializer = DeliveryContainsSerializer(contains, many=True)
        return Response(serializer.data)

class DeliveryContainsDelPharmDetail(APIView):
    def put(self, request, num, id, format=None):
        delivery = DeliveryContains.objects.filter(delivery=num)
        delivery2 = delivery.filter(pharmaceutical=id).first()
        serializer = DeliveryContainsSerializer(delivery2, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, id, format=None):
        delivery = DeliveryContains.objects.filter(delivery=num)
        delivery2 = delivery.filter(pharmaceutical=id).first()
        delivery2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarriedOutByView(APIView):
    def get(self, request, format=None):
        carried = CarriedOutBy.objects.all()
        serializer = CarriedOutBySerializer(carried, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarriedOutBySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarriedOutByDetail(APIView):
    def get(self, request, num, format=None):
        carried = CarriedOutBy.objects.filter(delivery=num).first()
        serializer = CarriedOutBySerializer(carried)
        return Response(serializer.data)

    def put(self, request, num, format=None):
        carried = CarriedOutBy.objects.filter(delivery=num).first()
        serializer = CarriedOutBySerializer(carried, data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, format=None):
        carried = CarriedOutBy.objects.filter(delivery=num)
        carried.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiagnosisView(APIView):
    def get(self, request, format=None):
        diagnosis = Diagnosis.objects.all()
        serializer = DiagnosisSerializer(diagnosis, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiagnosisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiagnosisPatientDetail(APIView):
    def get(self, request, num, format=None):
        diagnosis = Diagnosis.objects.filter(patient=num)
        serializer = DiagnosisSerializer(diagnosis, many=True)
        return Response(serializer.data)

    def delete(self, request, num, format=None):
        diagnosis = Diagnosis.objects.filter(patient=num)
        diagnosis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiagnosisPatientPharmDetail(APIView):
    def put(self, request, num, id, format=None):
        diagnosis = Diagnosis.objects.filter(patient=num)
        diagnosis2 = diagnosis.filter(pharmaceutical=id).first()
        serializer = DiagnosisSerializer(diagnosis2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, id, format=None):
        diagnosis = Diagnosis.objects.filter(patient=num)
        diagnosis2 = diagnosis.filter(pharmaceutical=id)
        diagnosis2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NurseOrderView(APIView):
    def get(self, request, format=None):
        order = NurseOrder.objects.all()
        serializer = NurseOrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NurseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NurseOrderPatientDetail(APIView):
    def get(self, request, num, format=None):
        order = NurseOrder.objects.filter(patient=num)
        serializer = NurseOrderSerializer(order, many=True)
        return Response(serializer.data)

    def delete(self, request, num, format=None):
        order = NurseOrder.objects.filter(patient=num)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NurseOrderPatientPharmDetail(APIView):
    def put(self, request, num, id, format=None):
        order = NurseOrder.objects.filter(patient=num)
        order2 = order.filter(pharmaceutical=id).first()
        serializer = NurseOrderSerializer(order2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, id, format=None):
        order = NurseOrder.objects.filter(patient=num)
        order2 = order.filter(pharmaceutical=id)
        order2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
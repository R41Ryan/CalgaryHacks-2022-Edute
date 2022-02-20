from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


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
    idSchool = models.OneToOneField(Account, primary_key=True, on_delete=CASCADE, related_name='driverAccountId')
    licenseNum = models.IntegerField()
    insurancePolicyNum = models.IntegerField()
    driverHistoryFilePath = models.FileField(upload_to="driverHistory")

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.idSchool)

class Posting(models.Model):
    postingId = models.AutoField(primary_key=True)
    startAddress = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    startTime = models.TimeField()
    endTime = models.TimeField()
    driverId = models.ForeignKey(Driver, on_delete=CASCADE, related_name="driverPostingId")
    maxPassenger = models.IntegerField()
    numOfPassenger = models.IntegerField()
    status = models.CharField(max_length=255)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.postingId)

class Report(models.Model):
    reportNum = models.AutoField(primary_key=True)
    reporterId = models.ForeignKey(Account, null=False, on_delete=CASCADE, related_name="reporterId")
    reportedId = models.ForeignKey(Account, null=False, on_delete=CASCADE, related_name="reportedId")

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.reportNum)

class PostingPassenger(models.Model):
    postingId = models.OneToOneField(Posting, null=False, on_delete=CASCADE, related_name="postingPassengerPosting")
    idPassenger = models.OneToOneField(Posting, null=False, on_delete=CASCADE, related_name="postingPassengerPassenger")

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.postingId) + " " + str(self.idPassenger)
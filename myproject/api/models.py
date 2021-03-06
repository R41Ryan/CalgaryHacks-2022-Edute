from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


# Create your models here.

class Account(models.Model):
    accountId = models.AutoField(primary_key=True)
    school = models.CharField(max_length=255)
    idSchool = models.IntegerField()
    phoneNum = models.IntegerField()
    imagePath = models.CharField(max_length=255)

    class Meta:
        app_label='api'
        unique_together = ("school", "idSchool")

    def __str__(self):
        return str(self.accountId)

class Driver(models.Model):
    accountId = models.OneToOneField(Account, primary_key=True, on_delete=CASCADE, related_name='driverAccountId')
    licenseNum = models.IntegerField()
    insurancePolicyNum = models.IntegerField()
    driverHistoryFilePath = models.CharField(max_length=255)

    class Meta:
        app_label='api'

    def __str__(self):
        return str(self.accountId)

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
        unique_together = ("postingId", "idPassenger")

    def __str__(self):
        return str(self.postingId) + " " + str(self.idPassenger)
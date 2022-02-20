# Generated by Django 4.0 on 2022-02-20 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('idSchool', models.IntegerField(primary_key=True, serialize=False)),
                ('phoneNum', models.IntegerField()),
                ('image', models.ImageField(upload_to='studentImages')),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('postingId', models.AutoField(primary_key=True, serialize=False)),
                ('startAddress', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('startTime', models.TimeField()),
                ('maxPassenger', models.IntegerField()),
                ('numOfPassenger', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Posting_Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPassenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='postingPassengerPassenger', to='api.posting')),
                ('postingId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='postingPassengerPosting', to='api.posting')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('reportNum', models.AutoField(primary_key=True, serialize=False)),
                ('reportedId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportedId', to='api.account')),
                ('reporterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporterId', to='api.account')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('idSchool', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='driverAccountId', serialize=False, to='api.account')),
                ('licenseNum', models.IntegerField()),
                ('insurancePolicyNum', models.IntegerField()),
                ('driverHistoryFilePath', models.FileField(upload_to='driverHistory')),
            ],
        ),
        migrations.AddField(
            model_name='posting',
            name='driverId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driverPostingId', to='api.driver'),
        ),
    ]

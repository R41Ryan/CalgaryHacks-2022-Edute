# Generated by Django 4.0 on 2021-12-22 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_medicinecasecontains_idpharmaceutical'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='IdPharmaceutical',
            new_name='idPharmaceutical',
        ),
        migrations.RenameField(
            model_name='medicalbed',
            old_name='Number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='medicalunit',
            old_name='Number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='medicinecasecontains',
            old_name='IdPharmaceutical',
            new_name='idPharmaceutical',
        ),
        migrations.RenameField(
            model_name='pharmaceutical',
            old_name='IdPharmaceutical',
            new_name='idPharmaceutical',
        ),
        migrations.RenameField(
            model_name='vitaminherb',
            old_name='IdPharmaceutical',
            new_name='idPharmaceutical',
        ),
        migrations.AlterUniqueTogether(
            name='medicalbed',
            unique_together={('number', 'medUnitNumber')},
        ),
        migrations.AlterUniqueTogether(
            name='medicinecasecontains',
            unique_together={('patientHealthcareNum', 'idPharmaceutical')},
        ),
    ]
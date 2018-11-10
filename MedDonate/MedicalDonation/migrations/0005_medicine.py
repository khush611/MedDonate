# Generated by Django 2.1.2 on 2018-11-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalDonation', '0004_assigned_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('mfgdate', models.DateField(auto_now=True)),
                ('expdate', models.DateField(auto_now=True)),
                ('manufacturer', models.CharField(max_length=64)),
                ('tradename', models.CharField(max_length=64)),
                ('composition', models.CharField(max_length=64)),
                ('uses', models.CharField(max_length=64)),
                ('quantity', models.PositiveIntegerField()),
                ('sideeffect', models.CharField(max_length=64)),
                ('saltcomposition', models.CharField(max_length=64)),
                ('dosage', models.CharField(max_length=64)),
            ],
        ),
    ]
# Generated by Django 2.1.2 on 2018-11-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalDonation', '0002_acceptor'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('RC_no', models.CharField(max_length=32)),
                ('registration_no', models.CharField(max_length=16)),
                ('last_servicing', models.DateField()),
                ('fuel_type', models.CharField(max_length=32)),
                ('insurence_no', models.CharField(max_length=32)),
                ('owner_name', models.CharField(max_length=32)),
                ('Date_purchase', models.DateField()),
                ('owner_number', models.IntegerField()),
            ],
        ),
    ]

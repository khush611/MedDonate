# Generated by Django 2.1.2 on 2018-11-10 17:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalDonation', '0011_auto_20181110_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine_ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indate', models.DateTimeField(default=datetime.datetime(2018, 11, 10, 23, 25, 0, 860434))),
                ('outdate', models.DateTimeField(default=datetime.datetime(2018, 11, 10, 23, 25, 0, 860434))),
                ('medicine_count', models.PositiveIntegerField(default=1)),
                ('acceptor_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='MedicalDonation.Acceptor')),
                ('collector_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='MedicalDonation.Collector')),
                ('donor_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='MedicalDonation.Doner')),
                ('medicine_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='MedicalDonation.medicine')),
            ],
        ),
        migrations.RemoveField(
            model_name='medicine_legger',
            name='acceptor_id',
        ),
        migrations.RemoveField(
            model_name='medicine_legger',
            name='collector_id',
        ),
        migrations.RemoveField(
            model_name='medicine_legger',
            name='donor_id',
        ),
        migrations.RemoveField(
            model_name='medicine_legger',
            name='medicine_id',
        ),
        migrations.DeleteModel(
            name='medicine_legger',
        ),
    ]
# Generated by Django 2.1.2 on 2018-11-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalDonation', '0005_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='collector',
            name='qualification',
            field=models.CharField(default='10th pass', max_length=64),
            preserve_default=False,
        ),
    ]

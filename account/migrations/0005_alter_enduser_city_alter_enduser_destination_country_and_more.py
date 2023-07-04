# Generated by Django 4.2.2 on 2023-07-04 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_enduser_body_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='city',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='destination_country',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
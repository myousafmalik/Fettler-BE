# Generated by Django 4.2.2 on 2023-06-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_batch_batch_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_name',
            field=models.IntegerField(choices=[(0, 'Bronze'), (1, 'Silver'), (2, 'Gold'), (3, 'Diamond')], default=1),
        ),
    ]

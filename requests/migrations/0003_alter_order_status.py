# Generated by Django 4.2.2 on 2023-06-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'PENDING'), (1, 'ACCEPTED'), (2, 'DELIVERED')], default=1),
        ),
    ]

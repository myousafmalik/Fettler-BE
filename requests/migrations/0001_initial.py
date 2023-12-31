# Generated by Django 4.2.2 on 2023-06-19 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.misc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=510)),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('estimated_profit', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to=utils.misc.request_image_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request_order', to='requests.request')),
                ('requestee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL)),
                ('rider', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rider_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

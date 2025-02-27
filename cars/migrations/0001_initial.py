# Generated by Django 4.2.15 on 2024-09-03 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('year_of_production', models.DateTimeField()),
                ('km', models.PositiveBigIntegerField()),
                ('descriptions', models.TextField(blank=True, max_length=300, null=True)),
                ('price', models.CharField(max_length=20)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static/')),
                ('car_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

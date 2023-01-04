# Generated by Django 4.1.4 on 2023-01-02 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_rename_fname_appointment_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='posicion_preferida',
            field=models.CharField(blank=True, choices=[('GK', 'Goalkeeper'), ('DF', 'Defender'), ('MF', 'Midfielder'), ('FW', 'Forward')], max_length=2),
        ),
    ]
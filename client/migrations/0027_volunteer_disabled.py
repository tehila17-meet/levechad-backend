# Generated by Django 3.0.4 on 2020-04-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0026_auto_20200417_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
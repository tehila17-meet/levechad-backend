# Generated by Django 3.0.4 on 2020-04-06 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_merge_20200403_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
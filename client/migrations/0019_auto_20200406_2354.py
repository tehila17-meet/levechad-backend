# Generated by Django 3.0.4 on 2020-04-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0018_auto_20200406_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='languages',
            field=models.ManyToManyField(to='client.Language'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_merge_20200402_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='volunteer_type',
            field=models.CharField(choices=[('NIGHBORHOOD_COORDINATOR', 'רכז שכונה'), ('CITY_COORDINATOR', 'רכז עיר'), ('STAFF', 'מטה'), ('HAMAL', 'חמל'), ('PROJECT', 'פרויקט'), ('CHILD_CARE', 'משפחתון'), ('AGRICULTURE', 'חקלאות'), ('MISSIONS', 'משימות')], default='MISSIONS', max_length=200),
        ),
    ]

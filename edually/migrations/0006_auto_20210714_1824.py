# Generated by Django 3.0.11 on 2021-07-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edually', '0005_auto_20210714_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseweek',
            name='add_to_calendar',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courseweek',
            name='reminder',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

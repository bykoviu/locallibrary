# Generated by Django 3.0.10 on 2020-11-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201031_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_of_dev',
            field=models.DateField(blank=True, null=True),
        ),
    ]

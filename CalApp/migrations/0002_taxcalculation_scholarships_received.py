# Generated by Django 4.1.7 on 2023-04-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxcalculation',
            name='scholarships_received',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

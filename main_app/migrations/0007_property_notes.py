# Generated by Django 3.0.8 on 2020-07-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200725_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='notes',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
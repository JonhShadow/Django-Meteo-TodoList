# Generated by Django 3.0.8 on 2020-07-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200729_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deadline_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
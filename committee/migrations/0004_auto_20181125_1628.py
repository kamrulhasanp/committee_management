# Generated by Django 2.1.2 on 2018-11-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0003_auto_20181125_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='descriptions',
            field=models.TimeField(max_length=1000),
        ),
    ]
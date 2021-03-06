# Generated by Django 2.1.2 on 2018-11-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0005_auto_20181125_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='leaderNumber',
            field=models.IntegerField(verbose_name='Leader Number'),
        ),
        migrations.AlterField(
            model_name='committee',
            name='memberNumber',
            field=models.IntegerField(verbose_name='Member Number'),
        ),
        migrations.AlterField(
            model_name='committee',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Committee Name'),
        ),
    ]

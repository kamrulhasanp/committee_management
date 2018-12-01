# Generated by Django 2.1.2 on 2018-11-25 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0002_auto_20181125_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='committee_photo')),
            ],
        ),
        migrations.RemoveField(
            model_name='committee',
            name='image',
        ),
        migrations.AddField(
            model_name='slideview',
            name='committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='committee.Committee'),
        ),
    ]
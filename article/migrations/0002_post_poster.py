# Generated by Django 2.0.7 on 2018-08-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
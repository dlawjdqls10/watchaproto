# Generated by Django 2.0.7 on 2018-08-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_post_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

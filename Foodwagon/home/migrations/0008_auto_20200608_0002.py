# Generated by Django 3.0.6 on 2020-06-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_request_first'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='first',
        ),
        migrations.AddField(
            model_name='review',
            name='first',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
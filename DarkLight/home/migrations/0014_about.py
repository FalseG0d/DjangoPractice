# Generated by Django 3.0.6 on 2020-05-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200531_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
    ]
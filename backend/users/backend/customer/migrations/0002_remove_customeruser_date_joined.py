# Generated by Django 4.1.7 on 2023-05-02 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='date_joined',
        ),
    ]
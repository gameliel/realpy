# Generated by Django 3.0.5 on 2020-05-02 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0003_auto_20200502_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='proerty_status',
            new_name='property_status',
        ),
    ]

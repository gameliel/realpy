# Generated by Django 3.0.5 on 2020-05-08 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0008_auto_20200508_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listingimage',
            old_name='listingid',
            new_name='listing',
        ),
    ]

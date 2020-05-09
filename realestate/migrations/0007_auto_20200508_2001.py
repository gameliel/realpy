# Generated by Django 3.0.5 on 2020-05-08 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0006_auto_20200503_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingimage',
            name='listingid',
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='listingimage',
            name='listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='realestate.Listing'),
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='image',
            field=models.ImageField(upload_to='listing/listpics/'),
        ),
    ]

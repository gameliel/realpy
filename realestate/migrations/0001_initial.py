# Generated by Django 3.0.5 on 2020-05-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_title', models.CharField(max_length=100)),
                ('proerty_status', models.CharField(choices=[('FR', 'For Rent'), ('FS', 'For Sale'), ('FL', 'For Lease')], default='FR', max_length=2)),
                ('property_type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('property_area', models.CharField(max_length=50)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('image', models.FileField(upload_to='uploads/')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField()),
                ('description', models.TextField()),
                ('date', models.TimeField()),
            ],
        ),
    ]
# Generated by Django 4.0 on 2022-04-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dbewskh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorghum', models.CharField(max_length=32)),
                ('safflower', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Dbewsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorghum', models.CharField(max_length=32)),
                ('safflower', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Dblwskh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chickpea', models.CharField(max_length=32)),
                ('rabi', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Dblwsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chickpea', models.CharField(max_length=32)),
                ('onion', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MbewkR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tomto', models.CharField(max_length=32)),
                ('fenugreek', models.CharField(max_length=32)),
                ('wheat', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Mbewskh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugarcane', models.CharField(max_length=32)),
                ('pigeonpea', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Mbewsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wheat', models.CharField(max_length=32)),
                ('sunflower', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Mblwskh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chickpea', models.CharField(max_length=32)),
                ('fenugreek', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Rbewkkh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groundnuts', models.CharField(max_length=32)),
                ('maize', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Rbewkr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gram', models.CharField(max_length=32)),
                ('raddish', models.CharField(max_length=32)),
                ('cabbage', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Rblwkkh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turi', models.CharField(max_length=32)),
                ('ragi', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Rblwkr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vatana', models.CharField(max_length=32)),
                ('raddish', models.CharField(max_length=32)),
                ('gram', models.CharField(max_length=32)),
            ],
        ),
    ]

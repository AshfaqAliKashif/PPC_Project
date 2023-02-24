# Generated by Django 4.0.10 on 2023-02-21 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('College_id', models.AutoField(primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('Division_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Division_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rolde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role_ID', models.IntegerField()),
                ('Role_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('District_ID', models.AutoField(primary_key=True, serialize=False)),
                ('District_Code', models.IntegerField(null=True)),
                ('District_Name', models.IntegerField(null=True)),
                ('District_Latitude', models.FloatField(null=True)),
                ('Distric_Longitude', models.FloatField(null=True)),
                ('Division_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PpcBackEnd.division')),
            ],
        ),
    ]
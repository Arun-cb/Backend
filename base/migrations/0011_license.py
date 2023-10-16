# Generated by Django 4.0.4 on 2023-07-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_kpi_user_access_kpi_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='license',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_key', models.CharField(max_length=50)),
                ('user_id', models.IntegerField(null=True)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_by', models.IntegerField()),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_sc_license',
            },
        ),
    ]
# Generated by Django 4.0.4 on 2023-03-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_kpi_actuals_perspective_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='smtp_configure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('server_name', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
                ('protocol', models.CharField(max_length=300)),
                ('port', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_by', models.IntegerField()),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.CharField(default='N', max_length=1)),
            ],
            options={
                'db_table': 'tb_sc_smtp_configure',
            },
        ),
    ]

# Generated by Django 4.0.4 on 2023-07-26 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_session_lasttime_alter_session_logintime'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=20)),
                ('show_flag', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('permission', models.ForeignKey(db_column='permission', on_delete=django.db.models.deletion.CASCADE, to='base.kpi_details')),
            ],
            options={
                'db_table': 'tb_sc_notification',
            },
        ),
    ]
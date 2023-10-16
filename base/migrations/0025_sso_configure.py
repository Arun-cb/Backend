# Generated by Django 4.0.4 on 2023-07-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_notification_notification_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='sso_configure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('app_id', models.CharField(max_length=300)),
                ('tenant_id', models.CharField(max_length=300)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_by', models.IntegerField()),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('delete_flag', models.CharField(default='N', max_length=1)),
            ],
            options={
                'db_table': 'tb_sc_sso_configure',
            },
        ),
    ]

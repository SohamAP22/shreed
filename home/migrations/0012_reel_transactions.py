# Generated by Django 4.2.1 on 2023-06-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_reel_entry_reel_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='reel_transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reel_no', models.IntegerField(null=True)),
                ('reel_time_date', models.DateTimeField(null=True)),
                ('reel_old_balance', models.IntegerField(default=0, null=True)),
                ('reel_new_balance', models.IntegerField(default=0, null=True)),
                ('reel_old_utilization', models.IntegerField(default=0, null=True)),
                ('reel_new_utilization', models.IntegerField(default=0, null=True)),
                ('reel_old_waste', models.IntegerField(default=0, null=True)),
                ('reel_new_waste', models.IntegerField(default=0, null=True)),
                ('reel_old_amount', models.IntegerField(default=0, null=True)),
                ('reel_new_amount', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_reel_entry_reel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reel_entry',
            name='reel_no',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_alter_registrar_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrar',
            name='date_of_birth',
            field=models.DateField(default='2023-02-01'),
        ),
    ]

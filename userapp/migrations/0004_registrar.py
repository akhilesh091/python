# Generated by Django 4.1.4 on 2023-09-06 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
        ('userapp', '0003_alter_advocate_type_of_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(default='2023-02-01')),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(default='not given', max_length=200)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='association.court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

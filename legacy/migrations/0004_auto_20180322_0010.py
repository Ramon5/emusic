# Generated by Django 2.0.2 on 2018-03-22 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legacy', '0003_auto_20180321_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresacontratante',
            name='UFEmpresa',
            field=models.CharField(blank=True, choices=[('MG', 'Minas Gerais'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro'), ('ES', 'Espirito Santo'), ('BA', 'Bahia')], max_length=3, null=True, verbose_name='Estado'),
        ),
    ]

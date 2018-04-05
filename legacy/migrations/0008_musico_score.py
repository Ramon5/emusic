# Generated by Django 2.0.2 on 2018-03-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legacy', '0007_auto_20180322_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='musico',
            name='Score',
            field=models.IntegerField(blank=True, choices=[('1', '1 Estrela (Muito Ruim)'), ('2', '2 Estrelas (Ruim)'), ('3', '3 Estrelas (Medio)'), ('4', '4 Estrelas (Bom)'), ('5', '5 Estrelas (Muito Bom)')], max_length=3, null=True, verbose_name='Score'),
        ),
    ]
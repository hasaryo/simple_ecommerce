# Generated by Django 5.0.1 on 2024-03-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0013_alter_produto_preco_marketing_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(blank=True, null=True, verbose_name='Preço Promo'),
        ),
    ]
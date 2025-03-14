# Generated by Django 5.1.7 on 2025-03-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0002_factorcoefficient_alter_rawmaterial_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='menu_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='product',
            name='percentage_cost',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='service_cost',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='suggested_price',
            field=models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=15),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='total',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=15),
        ),
    ]

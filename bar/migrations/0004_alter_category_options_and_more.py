# Generated by Django 5.1.7 on 2025-04-05 14:23

import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0003_product_menu_price_product_percentage_cost_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='factorcoefficient',
            options={'verbose_name': 'ضریب عامل', 'verbose_name_plural': 'ضرایب عامل'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'آیتم اصلی', 'verbose_name_plural': 'آیتم های اصلی'},
        ),
        migrations.AlterModelOptions(
            name='productdetails',
            options={'verbose_name': 'آماده سازی', 'verbose_name_plural': 'آماده سازی'},
        ),
        migrations.AlterModelOptions(
            name='rawmaterial',
            options={'verbose_name': 'ماده اولیه', 'verbose_name_plural': 'مواد اولیه'},
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='ثبت\u200cکننده'),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='بروزرسانی\u200cکننده'),
        ),
        migrations.AddField(
            model_name='factorcoefficient',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factorcoefficient',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='ثبت\u200cکننده'),
        ),
        migrations.AddField(
            model_name='factorcoefficient',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AddField(
            model_name='factorcoefficient',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='بروزرسانی\u200cکننده'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='ثبت\u200cکننده'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='بروزرسانی\u200cکننده'),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='ثبت\u200cکننده'),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='بروزرسانی\u200cکننده'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='ثبت\u200cکننده'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='بروزرسانی\u200cکننده'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=255, unique=True, verbose_name='نام انگلیسی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_fa',
            field=models.CharField(max_length=255, unique=True, verbose_name='نام فارسی'),
        ),
        migrations.AlterField(
            model_name='factorcoefficient',
            name='coefficient',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ضریب'),
        ),
        migrations.AlterField(
            model_name='factorcoefficient',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='factor_coefficient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bar.factorcoefficient', verbose_name='ضریب عامل'),
        ),
        migrations.AlterField(
            model_name='product',
            name='menu_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15, verbose_name='قیمت در منو'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='نام غذا'),
        ),
        migrations.AlterField(
            model_name='product',
            name='percentage_cost',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5, verbose_name='ضریب کاست'),
        ),
        migrations.AlterField(
            model_name='product',
            name='service_cost',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='هزینه سرویس'),
        ),
        migrations.AlterField(
            model_name='product',
            name='suggested_price',
            field=models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=15, verbose_name='قیمت پیشنهادی'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='price',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=10, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bar.product', verbose_name='غذا'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='quantity',
            field=models.FloatField(verbose_name='مقدار'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bar.rawmaterial', verbose_name='ماده خام'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='total',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=15, verbose_name='قیمت کل'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='unit',
            field=models.CharField(choices=[('quantity', 'تعداد'), ('gram', 'گرم'), ('kilogram', 'کیلوگرم'), ('milliliter', 'میلی لیتر'), ('liter', 'لیتر')], max_length=20, verbose_name='واحد'),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bar.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='نام ماده'),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='quantity',
            field=models.FloatField(verbose_name='مقدار'),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='total_price',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=10, verbose_name='قیمت کل'),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='unit',
            field=models.CharField(choices=[('quantity', 'تعداد'), ('gram', 'گرم'), ('kilogram', 'کیلوگرم'), ('milliliter', 'میلی لیتر'), ('liter', 'لیتر')], max_length=20, verbose_name='واحد'),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='unit_price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت واحد'),
        ),
        migrations.CreateModel(
            name='FoodAdditives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='نام افزودنی')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=15, verbose_name='قیمت کل')),
                ('total_quantity', models.FloatField(default=0, editable=False, verbose_name='مقدار')),
                ('price_per_kg', models.DecimalField(decimal_places=0, default=0, editable=False, max_digits=15, verbose_name='قیمت هر کیلو')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='ثبت\u200cکننده')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='بروزرسانی\u200cکننده')),
            ],
            options={
                'verbose_name': 'آیتم مخلفات',
                'verbose_name_plural': 'آیتم های مخلفات',
            },
        ),
        migrations.AddField(
            model_name='productdetails',
            name='additive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bar.foodadditives', verbose_name='افزودنی'),
        ),
        migrations.CreateModel(
            name='PriceFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('name', models.CharField(choices=[('menu_price', 'افزایش قیمت منو'), ('service_cost', 'افزایش هزینه سرویس')], max_length=255, unique=True, verbose_name='نام')),
                ('factor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ضریب')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='ثبت\u200cکننده')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='بروزرسانی\u200cکننده')),
            ],
            options={
                'verbose_name': 'ضریب افزایش / کاهش قیمت',
                'verbose_name_plural': 'ضرایب افزایش / کاهش قیمت',
            },
        ),
    ]

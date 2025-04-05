from django.db import models
from decimal import Decimal
from .middleware import get_current_user
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

User = get_user_model()


def user_str(self):
    return f"{self.first_name} {self.last_name} ({self.username})"

User.add_to_class("__str__", user_str)


class TimeStampedModel(models.Model):
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_%(class)s", verbose_name="ثبت‌کننده")
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_%(class)s", verbose_name="بروزرسانی‌کننده")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()

        if not self.pk and not self.created_by:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)


class Unit(models.TextChoices):
    QUANTITY = "quantity", "تعداد"
    GRAM = "gram", "گرم"
    KILOGRAM = "kilogram", "کیلوگرم"
    MILLILITER = "milliliter", "میلی لیتر"
    LITER = "liter", "لیتر"

class Category(TimeStampedModel):
    name_fa = models.CharField(max_length=255, unique=True, verbose_name="نام فارسی")
    name_en = models.CharField(max_length=255, unique=True, verbose_name="نام انگلیسی")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    
    def __str__(self):
        return self.name_fa + '_'  + self.name_en

class RawMaterial(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="نام ماده")
    unit = models.CharField(max_length=20, choices=Unit.choices, verbose_name="واحد")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی")
    quantity = models.FloatField(verbose_name="مقدار")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    unit_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت واحد")
    total_price = models.DecimalField(max_digits=10, decimal_places=0, editable=False, verbose_name="قیمت کل")

    class Meta:
        
        verbose_name = 'ماده اولیه'
        verbose_name_plural = 'مواد اولیه'

    def save(self, *args, **kwargs):
        if self.unit in [Unit.GRAM, Unit.MILLILITER]:
            self.total_price = (self.unit_price * Decimal(1000)) / Decimal(self.quantity)
        else:
            self.total_price = self.unit_price / Decimal(self.quantity)
        super().save(*args, **kwargs)

    def persian_total_price(self):
        return "ریال {:,}".format(self.total_price)
    persian_total_price.short_description = "قیمت کل"
    
    def __str__(self):
        return f"{self.name} ({self.category.name_fa})"
    
class FactorCoefficient(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="نام")
    coefficient = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="ضریب")

    class Meta:        
        verbose_name = 'ضریب عامل'
        verbose_name_plural = 'ضرایب عامل'
    
    def __str__(self):
        return f"{self.name} ({self.coefficient})"
    
class Product(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="نام غذا")
    factor_coefficient = models.ForeignKey(FactorCoefficient, on_delete=models.CASCADE, verbose_name="ضریب عامل")
    total_price = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False)
    service_cost = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="هزینه سرویس")
    suggested_price = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, verbose_name="قیمت پیشنهادی")
    menu_price = models.DecimalField(max_digits=15, decimal_places=0, default=0, verbose_name="قیمت در منو")
    percentage_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0, editable=False, verbose_name="ضریب کاست")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = 'آیتم اصلی'
        verbose_name_plural = 'آیتم های اصلی'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # ابتدا محصول ذخیره شود تا مقدار ID دریافت کند

        # محاسبه مقدار `total_price`
        total_price = sum(detail.total for detail in self.productdetails_set.all())

        # اگر مقدار `total_price` محاسبه شد، مقدارهای دیگر را به‌روز کنیم
        if total_price > 0:
            self.total_price = total_price
            self.suggested_price = (self.total_price * self.factor_coefficient.coefficient) + self.service_cost
            
            # محاسبه `percentage_cost` فقط در صورتی که `menu_price` مقدار معتبر داشته باشد
            if self.menu_price > 0:
                self.percentage_cost = (self.total_price / self.menu_price) * 100
            else:
                self.percentage_cost = 0  # جلوگیری از تقسیم بر صفر

            # ذخیره فیلدهای محاسبه‌شده
            super().save(update_fields=["total_price", "suggested_price", "percentage_cost"])
    
    def __str__(self):
        return self.name
    
    def get_categories(self):
        categories = self.productdetails_set.values_list('recipe__category__name_fa', flat=True).distinct()
        return " ⟶ ".join(categories) if categories else "بدون دسته‌بندی"

    get_categories.short_description = "دسته بندی"
    
    def persian_total_price(self):
        return "ریال {:,}".format(self.total_price)
    persian_total_price.short_description = "جمع هزینه"
    
    def persian_service_cost(self):
        return "ریال {:,}".format(self.service_cost)
    persian_service_cost.short_description = "هزینه سرویس"
    
    def persian_suggested_price(self):
        return "ریال {:,}".format(self.suggested_price)
    persian_suggested_price.short_description = "قیمت پیشنهادی"
    
    def persian_menu_price(self):
        return "ریال {:,}".format(self.menu_price)
    persian_menu_price.short_description = "قیمت در منو"


class FoodAdditives(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="نام افزودنی")
    total_price = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, verbose_name="قیمت کل")
    total_quantity = models.FloatField(verbose_name="مقدار", default=0, editable=False)
    price_per_kg = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, verbose_name="قیمت هر کیلو")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = 'آیتم مخلفات'
        verbose_name_plural = 'آیتم های مخلفات'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # ابتدا محصول ذخیره شود تا مقدار ID دریافت کند

        # محاسبه مقدار `total_price`
        total_price = sum(detail.total for detail in self.productdetails_set.all())
        total_quantity = sum(detail.quantity for detail in self.productdetails_set.all())
        print("total_price: ", total_price)
        print("total_quantity: ", total_quantity)
        # اگر مقدار `total_price` محاسبه شد، مقدارهای دیگر را به‌روز کنیم
        if total_price > 0:
            self.total_price = total_price
            self.total_quantity = total_quantity
            if total_quantity > 0:
                self.price_per_kg = (total_price/Decimal(total_quantity)) * 1000
            
            # ذخیره فیلدهای محاسبه‌شده
            super().save(update_fields=["total_price", "total_quantity", "price_per_kg"])
    
    def __str__(self):
        return self.name
    
    
    def persian_total_price(self):
        return "ریال {:,}".format(self.total_price)
    persian_total_price.short_description = "جمع هزینه"

    def persian_price_per_kg(self):
        return "ریال {:,}".format(self.price_per_kg)
    persian_price_per_kg.short_description = "هزینه هر کیلو"


class ProductDetails(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name="غذا")
    additive = models.ForeignKey(FoodAdditives, on_delete=models.CASCADE, null=True, blank=True, verbose_name="افزودنی")
    recipe = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, verbose_name="ماده خام")
    quantity = models.FloatField(verbose_name="مقدار")
    unit = models.CharField(max_length=20, choices=Unit.choices, verbose_name="واحد")
    price = models.DecimalField(max_digits=10, decimal_places=0, editable=False, verbose_name="قیمت")
    total = models.DecimalField(max_digits=15, decimal_places=0, editable=False, verbose_name="قیمت کل")

    class Meta:
        verbose_name = 'آماده سازی'
        verbose_name_plural = 'آماده سازی'


    def save(self, *args, **kwargs):

        self.price = self.recipe.total_price

        if self.unit == Unit.GRAM:
            self.total = (self.price * Decimal(self.quantity)) / Decimal(1000)
        else:
            self.total = self.price * Decimal(self.quantity)
        
        super().save(*args, **kwargs)  # ابتدا جزئیات محصول ذخیره شود
        
        # به‌روزرسانی مقدار `total_price` در `Product`
        if self.product:
            self.product.save()
        else:
            self.additive.save()

    def persian_price(self):
        return "ریال {:,}".format(self.price)
    persian_price.short_description = "قیمت"
    
    def persian_total(self):
        return "ریال {:,}".format(self.total)
    persian_total.short_description = "قیمت کل"
    
    def __str__(self):
        if self.product:
            return f"{self.product.name} - {self.recipe.name}"
        else:
            return f"{self.additive.name} - {self.recipe.name}"
    

class PriceFactor(TimeStampedModel):
    MENU_PRICE = 'menu_price'
    SERVICE_COST = 'service_cost'

    FACTOR_CHOICES = [
        (MENU_PRICE, 'افزایش قیمت منو'),
        (SERVICE_COST, 'افزایش هزینه سرویس')
    ]
    name = models.CharField(max_length=255, choices=FACTOR_CHOICES, unique=True, verbose_name="نام")
    factor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="ضریب")

    def __str__(self):
        return f"{self.name} - {self.factor} ({self.created_at.strftime('%Y-%m-%d')})"
    
    class Meta:
        verbose_name = 'ضریب افزایش / کاهش قیمت'
        verbose_name_plural = 'ضرایب افزایش / کاهش قیمت'
    
    @classmethod
    def get_latest_factor(cls, name):
        latest_factor = cls.objects.filter(name=name).order_by("-created_at").first()
        return latest_factor.factor if latest_factor else 1.0
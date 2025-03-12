from django.db import models
from decimal import Decimal

class Unit(models.TextChoices):
    QUANTITY = "quantity", "تعداد"
    GRAM = "gram", "گرم"
    KILOGRAM = "kilogram", "کیلوگرم"
    MILLILITER = "milliliter", "میلی لیتر"
    LITER = "liter", "لیتر"

class Category(models.Model):
    name_fa = models.CharField(max_length=255, unique=True)
    name_en = models.CharField(max_length=255, unique=True)

    
    def __str__(self):
        return self.name_fa + '_'  + self.name_en

class RawMaterial(models.Model):
    name = models.CharField(max_length=255, unique=True)
    unit = models.CharField(max_length=20, choices=Unit.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.FloatField()
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, editable=False)

    def save(self, *args, **kwargs):
        if self.unit in [Unit.GRAM, Unit.MILLILITER]:
            self.total_price = (self.unit_price * Decimal(1000)) / Decimal(self.quantity)
        else:
            self.total_price = self.unit_price / Decimal(self.quantity)
        super().save(*args, **kwargs)

    def persian_total_price(self):
        return "ریال {:,}".format(self.total_price)
    
    def __str__(self):
        return f"{self.name} ({self.category.name_fa})"
    
class FactorCoefficient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    coefficient = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ({self.coefficient})"
    
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    factor_coefficient = models.ForeignKey(FactorCoefficient, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False)
    service_cost = models.DecimalField(max_digits=10, decimal_places=0)
    suggested_price = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # ابتدا محصول ذخیره شود تا مقدار ID دریافت کند

        # محاسبه مقدار `total_price` فقط در صورتی که محصول دارای `ProductDetails` باشد
        total_price = sum(detail.total for detail in self.productdetails_set.all())
        
        # اگر مقدار `total_price` محاسبه شد، آن را به‌روز کنیم
        if total_price > 0:
            self.total_price = total_price
            self.suggested_price = (self.total_price * self.factor_coefficient.coefficient) + self.service_cost
            super().save(update_fields=["total_price", "suggested_price"])  # فقط این فیلدها را ذخیره کن
    
    def __str__(self):
        return self.name
    
    def persian_total_price(self):
        return "ریال {:,}".format(self.total_price)
    
    def persian_service_cost(self):
        return "ریال {:,}".format(self.service_cost)
    
    def persian_suggested_price(self):
        return "ریال {:,}".format(self.suggested_price)

class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, choices=Unit.choices)
    price = models.DecimalField(max_digits=10, decimal_places=0, editable=False)
    total = models.DecimalField(max_digits=15, decimal_places=0, editable=False)

    def save(self, *args, **kwargs):
        self.price = self.recipe.unit_price

        if self.unit == Unit.GRAM:
            self.total = (self.price * Decimal(self.quantity)) / Decimal(1000)
        else:
            self.total = self.price * Decimal(self.quantity)

        super().save(*args, **kwargs)  # ابتدا جزئیات محصول ذخیره شود
        
        # به‌روزرسانی مقدار `total_price` در `Product`
        self.product.save()

    def persian_price(self):
        return "ریال {:,}".format(self.price)
    
    def persian_total(self):
        return "ریال {:,}".format(self.total)
    
    def __str__(self):
        return f"{self.product.name} - {self.recipe.name}"

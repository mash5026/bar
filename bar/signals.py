from .models import FoodAdditives, RawMaterial, Category, Unit
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=FoodAdditives)
def create_rowmaterial(sender, instance, created,**kwargs):
    if created:
        category = Category.objects.filter(name_en="others").first()
        unit = Unit.KILOGRAM

        RawMaterial.objects.create(
            name = instance.name,
            unit = unit,
            category = category,
            quantity = 1,
            unit_price = instance.price_per_kg,
            total_price = instance.price_per_kg 
        )
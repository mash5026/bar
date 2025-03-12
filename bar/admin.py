from django.contrib import admin
from .models import Category, RawMaterial, Product, ProductDetails, FactorCoefficient

# Register your models here.
class ProductDetailsInline(admin.TabularInline):
    model = ProductDetails
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_fa", "name_en")
    search_fields = ("name_fa", "name_en")

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "unit", "category", "quantity", "unit_price", "persian_total_price")
    search_fields = ("name", "category__name")
    list_filter = ("unit", "category")


@admin.register(FactorCoefficient)
class FactorCoefficientAdmin(admin.ModelAdmin):
    list_display = ("name", "coefficient")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "get_categories", "persian_total_price", "factor_coefficient", "persian_service_cost", "persian_suggested_price", "persian_menu_price", "percentage_cost")
    search_fields = ("name",)
    list_display_links = ("get_categories", "name")
    inlines = [ProductDetailsInline]

@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ("product", "recipe", "quantity", "unit", "persian_price", "persian_total")
    search_fields = ("product__name", "recipe__name")
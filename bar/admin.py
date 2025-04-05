from django.contrib import admin
from .models import Category, RawMaterial, Product, ProductDetails, FactorCoefficient, PriceFactor, FoodAdditives
from django import forms
from django.db.models import F

admin.site.index_title = "به سامانه مدیریت هزینه محصولات خوش  آمدید"


class CategoryFilter(admin.SimpleListFilter):
     title = "دسته بندی"
     parameter_name = "category"

     def lookups(self, request, model_admin):
          categories = set(Product.objects.values_list("productdetails__recipe__category__name_fa", flat=True).distinct())
          return [(category, category) for category in categories if category]
     def queryset(self, request, queryset):
          if self.value():
               return queryset.filter(productdetails__recipe__category__name_fa=self.value()).distinct()
          return queryset

def increase_service_cost(modeladmin, request, queryset):
        factor = PriceFactor.get_latest_factor("service_cost")
        queryset.update(service_cost = F("service_cost") * factor)
increase_service_cost.short_description = "افزایش هزینه سرویس با مقدار دلخواه"


def increase_menu_price(modeladmin, request, queryset):
        factor = PriceFactor.get_latest_factor("menu_price")
        queryset.update(menu_price = F("menu_price") * factor)
increase_menu_price.short_description = "افزایش قیمت منو با مقدار دلخواه"


# Register your models here.
class ProductDetailsInline(admin.TabularInline):
    model = ProductDetails
    readonly_fields = ('additive','created_at', 'created_by', 'updated_at', 'updated_by')
    extra = 1


class ProductDetailsInline1(admin.TabularInline):
    model = ProductDetails
    readonly_fields = ('product','created_at', 'created_by', 'updated_at', 'updated_by')
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_fa", "name_en")
    search_fields = ("name_fa", "name_en")
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "unit", "category", "quantity", "unit_price", "persian_total_price")
    search_fields = ("name", "category__name")
    list_filter = ("unit", "category")
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')

@admin.register(FactorCoefficient)
class FactorCoefficientAdmin(admin.ModelAdmin):
    list_display = ("name", "coefficient")
    search_fields = ("name",)
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "get_categories", "persian_total_price", "factor_coefficient", "persian_service_cost", "persian_suggested_price", "persian_menu_price", "percentage_cost")
    search_fields = ("name",)
    list_filter = (CategoryFilter,)
    list_display_links = ("get_categories", "name")
    inlines = [ProductDetailsInline]
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    actions = [increase_service_cost, increase_menu_price]


@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ("product", "recipe", "quantity", "unit", "persian_price", "persian_total")
    search_fields = ("product__name", "recipe__name")
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')


@admin.register(PriceFactor)
class PriceFactorAdmin(admin.ModelAdmin):
     list_display = ("name", "factor")
     readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')


@admin.register(FoodAdditives)
class FoodAdditivesAdmin(admin.ModelAdmin):
     list_display = ("name", "persian_total_price", "total_quantity", "persian_price_per_kg")
     inlines = [ProductDetailsInline1]
     readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
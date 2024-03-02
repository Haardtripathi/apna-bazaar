from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product_type)
admin.site.register(Brand)




class ProductImageAdmin(admin.StackedInline):
    model =ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name' , 'price' ,'product_type']
    inlines = [ProductImageAdmin]


@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material_name']


admin.site.register(Product ,ProductAdmin)


admin.site.register(ProductImage)



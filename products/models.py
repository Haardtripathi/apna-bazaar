from django.db import models
from .views import *
from django.utils.text import slugify
from base.models import BaseModel
# Create your models here.

class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)
    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category ,self).save(*args , **kwargs)
    def __str__(self) -> str:
        return self.category_name
    


class SubCategory(BaseModel):
    subcategory_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category , on_delete=models.CASCADE , related_name="category")
    slug = models.SlugField(unique=True,null=True , blank=True)
    def save(self , *args , **kwargs):
        self.slug = slugify(self.subcategory_name)
        super(SubCategory ,self).save(*args , **kwargs)
    def __str__(self) -> str:
        return self.subcategory_name

class Product_type(BaseModel):
    product_type_name=models.CharField(max_length=100)
    subcategory=models.ForeignKey(SubCategory , on_delete=models.CASCADE , related_name="subcategory")
    slug = models.SlugField(unique=True,null=True , blank=True)
    def save(self , *args , **kwargs):
        self.slug = slugify(self.product_type_name)
        super(Product_type ,self).save(*args , **kwargs)
    def __str__(self) -> str:
        return self.product_type_name


class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.size_name
    

class Brand(BaseModel):
    brand_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.brand_name
    
class Material(BaseModel):
    material_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.material_name
    

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    product_type=models.ForeignKey(Product_type , on_delete=models.CASCADE , related_name="product_type")
    slug = models.SlugField(unique=True,null=True , blank=True,max_length=500)
    price = models.IntegerField(null=True, blank=True)
    ratings= models.IntegerField(null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    size_variant = models.ManyToManyField(SizeVariant , blank=True)
    material=models.ManyToManyField(Material,blank=True)
    brand=models.ForeignKey(Brand, blank=True,null=True, on_delete=models.CASCADE,related_name="brand")
    

    def save(self , *args , **kwargs):
        self.slug = slugify(self.product_name)
        super(Product ,self).save(*args , **kwargs)
    def __str__(self) -> str:
        return self.product_name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image =  models.ImageField(upload_to="product")



    
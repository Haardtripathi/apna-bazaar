from django.shortcuts import render
from products.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    

    return render(request,'apna-bazaar.html',{'categories':Category.objects.all()})



@csrf_exempt
def products(request,category_slug,):
    category = get_object_or_404(Category, slug=category_slug)
    # print(category)
    products=Product.objects.filter(product_type__subcategory__category__category_name__iexact=category)
    # print(products)
    type_list=['Men Tshirt','Men Shirts','Men Jeans']
    brand_list=['Allen Solly','Levis','Raymond','Peter England','Pepe Jeans','Diesel']
    fabric_list=['Cotton','Nylon','Silk','Linen','Cotton denim','Raw denim','Stretch denim']

    data=[]
    for product in products:
        data.append({
            'product_name':product.product_name,
                'id':product.id,

            'price':product.price,
            'ratings':product.ratings,
                    'slug':product.slug,

            'product_descriptions':product.product_description,
            'size_variant':product.size_variant.values_list('size_name', flat=True),
            'material':product.material.values_list('material_name', flat=True),
            'brand':product.brand,
        })
    # print(data)

    if request.method == 'POST':
        categories = request.POST.getlist('category')
        brand= request.POST.getlist('brand')
        material=request.POST.getlist('fabric')
        
        all_products=Product.objects.filter(product_type__subcategory__category__category_name__iexact=category)
        # print(price)
        for x in categories:
            all_products=all_products.filter(product_type__product_type_name__iexact=x)

        for x in brand:
            all_products=all_products.filter(brand__brand_name__iexact=x)

        for x in material:
            all_products=all_products.filter(material__material_name__iexact=x)
            

        if 'price' in request.POST:
            price=request.POST['price']
            if price=='LTH':
                all_products=all_products.order_by('price')
            elif price=='HTL':
                all_products=all_products.order_by('price')[::-1]
            else:
                all_products=all_products



        data=[]
        for product in all_products:
            data.append({
                'id':product.id,
                    'product_name':product.product_name,
                    'slug':product.slug,
                        'price':product.price,
                        'ratings':product.ratings,
                        'product_descriptions':product.product_description,
                        'size_variant':product.size_variant.values_list('size_name', flat=True),
                        'material':product.material.values_list('material_name', flat=True),
                        'brand':product.brand,
                    })
            # print(data)
        
            
        return render(request, 'products.html',{'data':data,'type_list':type_list,'category':category,'brand_list':brand_list,'fabric_list':fabric_list})
        
        
        
    # print(product_types)

    return render(request, 'products.html',{'data':data,'type_list':type_list,'category':category,'brand_list':brand_list,'fabric_list':fabric_list})




def product_details(request,pk):
    product=Product.objects.get(id=pk)
    data={
                    'product_name':product.product_name,
                        'price':product.price,
                        'ratings':product.ratings,
                    'slug':product.slug,

                        'product_descriptions':product.product_description,
                        'size_variant':product.size_variant.values_list('size_name', flat=True),
                        'material':product.material.values_list('material_name', flat=True),
                        'brand':product.brand,
                    }
    return render(request, 'product_details.html',data)
    print(data)
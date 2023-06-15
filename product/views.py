from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def get_product(request):
    try:
        product_objs = Product.objects.all()
 
###### Sort by market price 

        if(request.GET.get('sortby')):
            sort_by = request.GET.get('sortby')
            if sort_by == "low":
                product_objs = product_objs.order_by('market_price')
            elif sort_by == "high":
                 product_objs = product_objs.order_by('-market_price')
                 
###### Seacrh by category

        if(request.GET.get('category')):
            category = request.GET.get('category')
            product_objs = Product.objects.filter(category = category)
###### Seacrh by title

        if(request.GET.get('title')):
            title = request.GET.get('title')
            product_objs = Product.objects.filter(title__icontains = title)

###### Seacrh by description

        if(request.GET.get('description')):
            description = request.GET.get('description')
            product_objs = Product.objects.filter(description__icontains = description)

        payload = []
        for product in product_objs:
            payload.append({
                "Title":product.title,
                "description":product.description,
                "selling_price":str(product.selling_price),
                "market_price":str(product.market_price),
                "cateory":product.category,
                "image":str(product.images),

            })
        return JsonResponse(payload, safe = False )

    except Exception as e:
        print(e)
        return JsonResponse({"message":"Something went wrong!"})    




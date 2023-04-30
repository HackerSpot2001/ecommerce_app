from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer
from string import ascii_uppercase, digits
from random import choice
from django.db.models import Q 
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from time import time
# Create your views here.


""" API to get all endpoinds """
@api_view(['GET'])
def endpoints(req):
    data = ["/list_products","/get_product/:name",'/create_product',"/update_product",'/delete_product',"/productpage"]
    return Response(data,status=200)



""" Route to get html product page """
@api_view(['GET'])
def productpage(req):
    return render(req,'index.html')



""" API to get details of a particular product """ 
@api_view(['GET'])
def get_product(req,product):
    try:
        products_rs = Product.objects.get(Q(product_id=product) & Q(is_active=True))
        serialized_data = ProductSerializer(products_rs) 
        response = {"apiresponse":{"type":"OK","message":"Operation completed successfully.","severity":"INFO"}}
        response["records"] = serialized_data.data

    except Exception as e:
        print("Error: ", str(e))
        response = {"apiresponse":{"type":"ERROR","severity":"ERROR","message":"There is some error."}}
        

    return Response(response,status=200)



""" API to get all products """ 
@api_view(['GET'])
def list_products(req):
    strtime = time()
    try:
        products_rs = Product.objects.filter(is_active=True).all()
        serialized_data = ProductSerializer(products_rs,many=True) 
        response = {"apiresponse":{"type":"OK","message":"Operation completed successfully.","severity":"INFO"}}
        response["records"] = serialized_data.data

    except Exception as e:
        print("Error: ", str(e))
        response = {"apiresponse":{"type":"ERROR","severity":"ERROR","message":"There is some error."}}
        
    ftime = time() - strtime
    print(ftime)
    return Response(response,status=200)



""" API to delete product """ 
@api_view(http_method_names=['GET',"POST"])
def delete_product(req):
    try:
        if req.method=='POST':
            products_rs = Product.objects.get(product_id = req.data['product_id'])
            # if (products_rs != Non?We) and (products_rs.created_by == req.user):
            if (products_rs != None):
                products_rs.is_active = False
                products_rs.save()
                response = {"apiresponse":{"type":"OK","message":"Operation completed successfully.","severity":"INFO"}}


            else:
                response = {"apiresponse":{"type":"ERROR","severity":"ERROR","message":"There is some error."}}


        else:
            response = {"apiresponse":{"type":"DEBUG","message":"Operation completed successfully.","severity":"DEBUG"}}


    except Exception as e:
        print("Error: ", str(e))
        response = {"apiresponse":{"type":"ERROR","severity":"ERROR","message":"There is some error."}}
        
    return Response(response,status=200)



""" API to create products """
@api_view(http_method_names=['GET','POST'])
def create_product(req):
    try:
        fields = [ "category" , "product_title" , "product_description" , "product_price" , "product_image" , "currency" , "discounted_value" , "discounted_type" ]
        if (req.method == 'POST'):
            jsondata = verify_fields(fields,dict(req.data))
            if jsondata['category'] == "":
                jsondata['category'] = "GENERAL"

            product_id =gen_id(initials="PRD_",length=20)
            category = Category.objects.get(category_id=jsondata['category'])
            product = Product.objects.create(
                # created_by = req.user,
                product_id = product_id,
                category = category,
                product_title = jsondata['product_title'] ,
                product_description = jsondata['product_description'],
                product_price = jsondata['product_price'],
                currency = jsondata['currency'],
                discounted_value = jsondata['discounted_value'],
                discounted_type = jsondata['discounted_type'],
            )
            serialized_data = ProductSerializer(product)
            response = {"apiresponse": {"type":"OK","message":"Operation completed successfully.","severity":"INFO"}, "record":serialized_data.data}

        else:
            response = {"apiresponse":{"type":"DEBUG","message":"Operation completed successfully.","severity":"DEBUG"}}

    except Exception as e:
        response = {"apiresponse":{"type":"ERROR","severity":"ERROR","message":"There is some error."}}
        print("Error: ",str(e))
    
    return Response(response,status=200)



""" API to update products """
@api_view(['GET','POST'])
def update_product(req):
    try:
        required_fields = [  "product_id" , "category" , "product_title" , "product_description" , "product_price" , "product_image" , "currency" , "discounted_value" , "discounted_type" ]
        if (req.method == 'POST'):
            jsondata    = verify_fields(required_fields,dict(req.data))
            category    = Category.objects.get(category_id =jsondata['category'])
            product     = Product.objects.get(product_id = jsondata["product_id"])
            # if product != None and product.created_by == req.user :
            if product != None :
                product.product_title           = jsondata['product_title'] 
                product.product_description     = jsondata['product_description'] 
                product.product_price           = jsondata['product_price'] 
                product.currency                = jsondata['currency'] 
                product.discounted_type         = jsondata['discounted_type'] 
                product.discounted_value        = jsondata['discounted_value'] 
                product.category                = category
                product.last_updated            = datetime.now()
                product.save()

                serialized_data = ProductSerializer(product)
                response = {"apiresponse": {"type":"OK","message":"Operation completed successfully.","severity":"INFO"}, "record":serialized_data.data}
    
            else:
                response = {"apiresponse":{"type":"ERROR","severity":"ERROR","message":"There is some error."}}

        else:
            response = {"apiresponse":{"type":"DEBUG","message":"Operation completed successfully.","severity":"DEBUG"}}

    except Exception as e:
        response = {"apiresponse":{"type":"ERROR","severity":"ERROR","message":"There is some error."}}
        print("Error: ",str(e))
    
    return Response(response,status=200)


def gen_id(initials="",length=15):
    chars= ascii_uppercase + digits
    return initials + ''.join(choice(chars) for _ in range(length))  


def verify_fields (fields:list,data:dict):  
    for i in fields:
        if i not in data.keys():
            data[i] = ""

    return dict(data)
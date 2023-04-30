from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_id                  = models.CharField(primary_key=True,unique=True,max_length=50)
    category_description         = models.TextField(null=True)
    created_by                   = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date                 = models.DateTimeField(auto_now=True)
    last_updated                 = models.DateTimeField(auto_now=True)

    class Meta:
        ordering   = ['-last_updated']

    def __str__(self):
        return self.category_id


class Product(models.Model):
    product_id                  = models.CharField(primary_key=True,unique=True,max_length=30)
    product_title               = models.CharField(max_length=255)
    product_description         = models.TextField(null=True)
    product_image               = models.ImageField(upload_to='static/uploads/',null=True)
    product_price               = models.FloatField(max_length=10)
    currency                    = models.CharField(max_length=20,null=True,choices=(('IN',"Indian Rupee"),('USD',"US Dollar")))          
    discounted_value            = models.IntegerField(null=True)
    discounted_type             = models.CharField(max_length=10,choices=(('pct',"Percentage"),('amt',"Amount")))          
    is_active                   = models.BooleanField(default=True)
    category                    = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_by                  = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_date                = models.DateTimeField(auto_now=True)
    last_updated                = models.DateTimeField(auto_now=True)

    class Meta:
        ordering   = ['-last_updated']

    def __str__(self):
        return self.product_id
from django.db import models
from .category import Category
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/') 
    price = models.FloatField()
    description=models.CharField(max_length=100,default='',null=True,blank=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products();
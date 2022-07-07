from django.db import models

# Create your models here.
class Seller(models.Model):
    GENDER_TYPES = (
            ('M', 'Male'),
            ('F', 'Female'),
            )
    PACKAGE_TYPES = (
            ('inihaw', 'inihaw package'),
            ('classic', 'classic package'),
            ('fried', 'fried package'),
            ('other', 'other package'),
            )
    Seller_Name = models.CharField(max_length=254)
    Seller_Contact = models.CharField(max_length=11)
    Address = models.CharField(max_length=254)
    Gender = models.CharField(max_length=1,choices=GENDER_TYPES)
    CustomerPackageType = models.CharField(max_length=254, choices=PACKAGE_TYPES)

    def __str__(self):
        return self.Seller_Name

class Sell(models.Model):
    Product_name= models.CharField(max_length=24)
    Product_amount= models.PositiveIntegerField()
    Product_price= models.PositiveIntegerField()
    Product_detail= models.TextField(blank=True)

    def __str__(self):
        return self.Product_name


class Order(models.Model):
    STATUS_TYPES = (
            ('delivered', 'delivered'),
            ('for pickup', 'for pickup'),
            ('done', 'done'),
            )
    Custumer_id= models.ForeignKey(Seller,on_delete = models.CASCADE)
    Product_id= models.ForeignKey(Sell,on_delete = models.CASCADE)
    Order_Date = models.DateField()
    Order_Price = models.PositiveIntegerField(blank = True)
    Order_Detail = models.TextField(blank = True)
    Order_Status = models.TextField(choices=STATUS_TYPES,default='for pickup')

    def __str__(self):
        return '%s-%s' % (self.Product_id, self.Custumer_id)

class Delivery(models.Model):
	Order_id = models.ForeignKey(Order,on_delete = models.CASCADE)
	Seller_Name = models.ForeignKey(Seller,on_delete = models.CASCADE)	
	Product_Name = models.ForeignKey(Sell,on_delete = models.CASCADE)
	Delivery_Address = models.TextField(blank = True)
	Delivery_Price = models.PositiveIntegerField(blank = True)
	Delivery_Date = models.DateField()

class Review(models.Model):
    RATINGS = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            )
    Seller_Reference = models.ForeignKey(Seller,on_delete = models.CASCADE)	
    Product_Reference = models.ForeignKey(Sell,on_delete = models.CASCADE)
    Review_Rating = models.CharField(choices=RATINGS,max_length=1,blank = True)
    Review_Comment = models.TextField(blank = True)
    Review_Suggestion = models.TextField(blank = True)

    def __str__(self):
        return self.Review_Comment

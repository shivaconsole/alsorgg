from email.policy import default
from pyexpat import model
from random import choices
from secrets import choice
from turtle import Turtle, width
from django.db import models
from customers.models import Customer
# Create your models here.
#from .forms import QuotationForm

class Quotation(models.Model):
    PRODUCT = (('WARDROBE-GST@18%', 'Wardrobe-GST@18%'),
               ('FURNITURE-GST@18%', 'Furniture-GST@18%'),
               ('KITCHEN-GST@18%', 'Kitchen-GST@18%'),
               ('DOOR-GST@18%', 'Door-GST%18%'),
               ('VANITY-GST@18%', 'Vanity-GST%18%'),
               ('PANELLING-GST@18%', 'Panelling-GST@18%'),
               ('SERVICE-GST@18%', 'Service-GST@18%'),
               ('ADDITIONAL-GST@18%', 'Additional-GST@18%'),)
    CHOICES_SAL = (('Mr.', 'MR.'), ('Mrs.', 'MRS.'), ('Shri', 'SHRI'), ('Shrimati', 'SHRIMATI'))

    Dated = models.DateTimeField(auto_now_add=True)
    salutation = models.CharField(max_length=20, choices=CHOICES_SAL, default=None, null=True)
    name = models.CharField(max_length=30, default=None)
    product = models.CharField(max_length=100, choices=PRODUCT, default=None, null=True)
    productDrNo = models.IntegerField()
    reference = models.CharField(max_length=100)
    designer = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, default=None)
    building = models.CharField(max_length=50)
    floor = models.CharField(max_length=30)
    landmark = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    remark = models.TextField()
    customerGST = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pinCode = models.IntegerField()



    def __str__(self):
        return f"{self.salutation} {self.name}"

# PRODUCT = (('WARDROBE-GST@18%', 'Wardrobe-GST@18%'),
        #        ('FURNITURE-GST@18%', 'Furniture-GST@18%'),
        #        ('KITCHEN-GST@18%', 'Kitchen-GST@18%'),
        #        ('DOOR-GST@18%', 'Door-GST@18%'),
        #        ('VANITY-GST@18%', 'Vanity-GST@18%'),
        #        ('PANELLING-GST@18%', 'Panelling-GST@18%'),
        #        ('SERVICE-GST@18%', 'Service-GST@18%'),
        #        ('ADDITIONAL-GST@18%', 'Additional-GST@18%'),)

# class Blockbtn(models.Model):
#         desc = models.CharField(max_length=70, null=True, default=None,choices=PRODUCT)
#         def __str__(self):
#              return self.desc



#     UNIT = (('MTR','mtr'),
#             ('RTF','rtf'),
#             ('SQFT','sqft'),
#             ('MM','mm'),
#             ('NOS','nos'),
#             ('RTFX2','rtfx2'),
#     )

#     PAY = (
#             ('PAID','paid'),
#             ('FOC','foc'),
#     )
class BlockItem(models.Model):
    desc = models.CharField(max_length=255,  null=True, default=None)
    finish = models.TextField()
    unit = models.CharField(max_length=20, null=True, default=None)
    width = models.IntegerField(null=True, default=None)
    height = models.IntegerField(null=True, default=None)
    qty = models.IntegerField(null=True, default=None)
    rate = models.IntegerField(null=True, default=None)
    payType = models.CharField(max_length=20, null=True, default=None)
    img = models.ImageField(upload_to='blockImg/Img/')
    def __str__(self):
        return f"{self.desc} {self.rate}"

class Appliance(models.Model):
    brand = models.CharField(max_length=100, null=True, default=None)
    desc = models.TextField()
    unit = models.CharField(max_length=30, null=True, default=None)
    price = models.IntegerField()
    qty = models.IntegerField()
    payType = models.CharField(max_length=30, null=True,default=None)
    img = models.ImageField(upload_to='applianceImg/Img/')
    def __str__(self):
        return f"{ self.brand} {self.desc}"
    

class Fitting(models.Model):
    brand = models.CharField(max_length=100, null=True, default=None)
    desc = models.TextField()
    unit = models.CharField(max_length=30, null=True, default=None)
    price = models.IntegerField()
    qty = models.IntegerField()
    payType = models.CharField(max_length=30, null=True,default=None)
    img = models.ImageField(upload_to='FittingImg/Img/')
    def __str__(self):
        return f"{ self.brand} {self.desc}"

class WoodworkDiscount(models.Model):
    wType = models.CharField(max_length=30, null=True, default=None)
    wValue = models.IntegerField()
    wPercent = models.IntegerField()
    def __str__(self):
        return f" {self.wType} - {self.wValue} - {self.wPercent}% "
    

class FittingDiscount(models.Model):
    fType = models.CharField(max_length=30, null=True, default=None)
    fValue = models.IntegerField()
    fPercent = models.IntegerField()
    def __str__(self):
        return f" {self.fType} - {self.fValue} - {self.fPercent}% "

class AppliancekDiscount(models.Model):
    aType = models.CharField(max_length=30, null=True, default=None)
    aValue = models.IntegerField()
    aPercent = models.IntegerField()
    def __str__(self):
        return f" {self.aType} - {self.aValue} - {self.aPercent}% "

class PackingDiscount(models.Model):
    pType = models.CharField(max_length=30, null=True, default=None)
    pValue = models.IntegerField()
    pPercent = models.IntegerField()
    def __str__(self):
        return f" {self.pType} - {self.pValue} - {self.pPercent}% "

class OtherDiscount(models.Model):
    cartage = models.IntegerField()
    installation = models.IntegerField()
    special_dis = models.IntegerField()
    def __str__(self):
        return f" {self.cartage} {self.installation} {self.special_dis} "

from django.db import models

# Create your models here.

class BelongstoBusinnesnit(models.Model):
    CHOICES_BU = (('FACTORY-UNIT', 'Factory-Unit'), ('CALLISTO-ELEMENT', 'Callisto-Element'))
    belongs_to_business_unit = models.CharField(max_length=100, choices=CHOICES_BU)

    def __str__(self):
        return self.belongs_to_business_unit

class Customer(models.Model):
    CHOICES_SAL = (('Mr.', 'MR.'), ('Mrs.', 'MRS.'), ('Shri', 'SHRI'), ('Shrimati', 'SHRIMATI'))

    salutation = models.CharField(max_length=20, choices=CHOICES_SAL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cust_image = models.ImageField()
    email_id = models.EmailField()
    contactno = models.CharField(max_length=15)
    belongstounit = models.ForeignKey(BelongstoBusinnesnit, on_delete=models.SET_NULL, default=None, null=True)
    building = models.CharField(max_length=20)
    floor = models.CharField(max_length=20)
    landmark = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.salutation + self.first_name +self.last_name
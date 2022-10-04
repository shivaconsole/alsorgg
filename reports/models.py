from django.db import models

# Create your models here.
class ReportDB(models.Model):
    # PRODUCT = (('WARDROBE-GST@18%', 'Wardrobe-GST@18%'),
    #            ('FURNITURE-GST@18%', 'Furniture-GST@18%'),
    #            ('KITCHEN-GST@18%', 'Kitchen-GST@18%'),
    #            ('DOOR-GST@18%', 'Door-GST@18%'),
    #            ('VANITY-GST@18%', 'Vanity-GST@18%'),
    #            ('PANELLING-GST@18%', 'Panelling-GST@18%'),
    #            ('SERVICE-GST@18%', 'Service-GST@18%'),
    #            ('ADDITIONAL-GST@18%', 'Additional-GST@18%'),)

    srno = models.IntegerField(null=False)
    desc = models.CharField(max_length=100, default=None, null=True)
    finish = models.CharField(max_length=350)
    refImg = models.ImageField(upload_to='reports/image/')
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    area = models.CharField(max_length=50)
    uqm = models.CharField(max_length=50)
    qty = models.IntegerField()
    rate = models.DecimalField(max_digits=7, decimal_places=2)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.desc
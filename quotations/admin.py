from django.contrib import admin
from .models import Quotation, BlockItem,Appliance,Fitting,WoodworkDiscount,AppliancekDiscount,FittingDiscount,PackingDiscount,OtherDiscount
# Register your models here.
admin.site.register(Quotation)
admin.site.register(BlockItem)
admin.site.register(Appliance)
admin.site.register(Fitting)
admin.site.register(WoodworkDiscount)
admin.site.register(AppliancekDiscount)
admin.site.register(FittingDiscount)
admin.site.register(PackingDiscount)
admin.site.register(OtherDiscount)
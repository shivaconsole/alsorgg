from django.contrib import admin
from .models import User, Lead, Agent, LeadStatusCode, ProductCategory, LeadCategoryCode

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
#admin.site.register(Belongstounit)

class LeadStatusCodeAdmin(admin.ModelAdmin):
    list_per_page = 100
    show_full_result_count = False
    list_display = [f.name for f in LeadStatusCode._meta.fields]
admin.site.register(LeadStatusCode, LeadStatusCodeAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_per_page = 100
    show_full_result_count = False
    list_display = [f.name for f in ProductCategory._meta.fields]
admin.site.register(ProductCategory, ProductCategoryAdmin)

class LeadCategoryCodeAdmin(admin.ModelAdmin):
    list_per_page = 100
    show_full_result_count = False
    list_display = [f.name for f in LeadCategoryCode._meta.fields]
admin.site.register(LeadCategoryCode, LeadCategoryCodeAdmin)
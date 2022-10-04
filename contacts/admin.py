from django.contrib import admin

# Register your models here.
from .models import ContactCategoryCode, StatusCode, BelongstoBusinnesnit, Contact

admin.site.register(Contact)
admin.site.register(BelongstoBusinnesnit)

class StatusCodeAdmin(admin.ModelAdmin):
    list_per_page = 100
    show_full_result_count = False
    list_display = [f.name for f in StatusCode._meta.fields]
admin.site.register(StatusCode, StatusCodeAdmin)


'''
class LeadStatusCodeAdmin(admin.ModelAdmin):
    list_per_page = 100
    show_full_result_count = False
    list_display = [f.name for f in LeadStatusCode._meta.fields]
admin.site.register(LeadStatusCode, LeadStatusCodeAdmin)'''

class ContactCategoryCodeAdmin(admin.ModelAdmin):
    list_per_page = 100
    show_full_result_count = False
    list_display = [f.name for f in ContactCategoryCode._meta.fields]
admin.site.register(ContactCategoryCode, ContactCategoryCodeAdmin)


from django.db import models

# Create your models here.
CURR_STATE = (('ACTIVE-ACTIVE', 'ACTIVE-Active'), ('INACTIVE-INACTIVE', 'INACTIVE-Inactive'))
CON_CATEGORY_GROUP = (('VENDORS', 'Vendors'), ('SERVICE', 'Service'), ('AUDIT and ACCOUNTS', 'Audit and Accounts'), ('TECHNICAL-ARCHITECTS and DESIGNERS', 'Technical- Architects and Designers'), ('FRIENDS - FRIENDS AND FAMILY MEMBERS', 'Friends and Family Members'))


class ContactCategoryCode(models.Model):
    contact_category_group = models.CharField(max_length=100, choices=CON_CATEGORY_GROUP)
    category_code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_code

class StatusCode(models.Model):
    current_state = models.CharField(max_length=100, choices=CURR_STATE)
    status_code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.status_code

class BelongstoBusinnesnit(models.Model):
    CHOICES_BU = (('FACTORY-UNIT', 'Factory-Unit'), ('CALLISTO-ELEMENT', 'Callisto-Element'))
    belongs_to_business_unit = models.CharField(max_length=100, choices=CHOICES_BU)

    def __str__(self):
        return self.belongs_to_business_unit


class Contact(models.Model):
    CHOICES_SAL = (('Mr.', 'MR.'), ('Mrs.', 'MRS.'), ('Shri', 'SHRI'), ('Shrimati', 'SHRIMATI'))

    title = models.CharField(max_length=10, choices=CHOICES_SAL)
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    primary_contact_number = models.CharField(max_length=30)
    alternate_contact_number = models.CharField(max_length=30)
    primary_email = models.EmailField()
    alternate_email = models.EmailField()
    current_state = models.CharField(max_length=100, choices=CURR_STATE, default=None, null=True)
    status_code = models.ForeignKey(StatusCode, on_delete=models.SET_NULL, default=None, null=True)
    contact_category_group = models.CharField(max_length=100, choices=CON_CATEGORY_GROUP, default=None, null=True)
    contact_category = models.ForeignKey(ContactCategoryCode, on_delete=models.SET_NULL, default=None, null=True)
    belongs_to_business_unit = models.ForeignKey(BelongstoBusinnesnit, on_delete=models.SET_NULL, default=None, null=True)
    notes = models.TextField()

    address = models.TextField()

    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


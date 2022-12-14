# Generated by Django 4.1 on 2022-09-21 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BelongstoBusinnesnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belongs_to_business_unit', models.CharField(choices=[('FACTORY-UNIT', 'Factory-Unit'), ('CALLISTO-ELEMENT', 'Callisto-Element')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactCategoryCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_category_group', models.CharField(choices=[('VENDORS', 'Vendors'), ('SERVICE', 'Service'), ('AUDIT and ACCOUNTS', 'Audit and Accounts'), ('TECHNICAL-ARCHITECTS and DESIGNERS', 'Technical- Architects and Designers'), ('FRIENDS - FRIENDS AND FAMILY MEMBERS', 'Friends and Family Members')], max_length=100)),
                ('category_code', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_state', models.CharField(choices=[('ACTIVE-ACTIVE', 'ACTIVE-Active'), ('INACTIVE-INACTIVE', 'INACTIVE-Inactive')], max_length=100)),
                ('status_code', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('title', models.CharField(choices=[('Mr.', 'MR.'), ('Mrs.', 'MRS.'), ('Shri', 'SHRI'), ('Shrimati', 'SHRIMATI')], max_length=10)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('primary_contact_number', models.CharField(max_length=30)),
                ('alternate_contact_number', models.CharField(max_length=30)),
                ('primary_email', models.EmailField(max_length=254)),
                ('alternate_email', models.EmailField(max_length=254)),
                ('current_state', models.CharField(choices=[('ACTIVE-ACTIVE', 'ACTIVE-Active'), ('INACTIVE-INACTIVE', 'INACTIVE-Inactive')], default=None, max_length=100, null=True)),
                ('contact_category_group', models.CharField(choices=[('VENDORS', 'Vendors'), ('SERVICE', 'Service'), ('AUDIT and ACCOUNTS', 'Audit and Accounts'), ('TECHNICAL-ARCHITECTS and DESIGNERS', 'Technical- Architects and Designers'), ('FRIENDS - FRIENDS AND FAMILY MEMBERS', 'Friends and Family Members')], default=None, max_length=100, null=True)),
                ('notes', models.TextField()),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('belongs_to_business_unit', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.belongstobusinnesnit')),
                ('contact_category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contactcategorycode')),
                ('status_code', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.statuscode')),
            ],
        ),
    ]

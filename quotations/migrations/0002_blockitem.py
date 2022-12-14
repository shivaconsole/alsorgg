# Generated by Django 4.1 on 2022-09-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(choices=[('WARDROBE-GST@18%', 'Wardrobe-GST@18%'), ('FURNITURE-GST@18%', 'Furniture-GST@18%'), ('KITCHEN-GST@18%', 'Kitchen-GST@18%'), ('DOOR-GST@18%', 'Door-GST%18%'), ('VANITY-GST@18%', 'Vanity-GST%18%'), ('PANELLING-GST@18%', 'Panelling-GST@18%'), ('SERVICE-GST@18%', 'Service-GST@18%'), ('ADDITIONAL-GST@18%', 'Additional-GST@18%')], default=None, max_length=70, null=True)),
                ('finish', models.TextField()),
                ('unit', models.CharField(choices=[('MTR', 'mtr'), ('RTF', 'rtf'), ('SQFT', 'sqft'), ('MM', 'mm'), ('NOS', 'nos'), ('RTFX2', 'rtfx2')], default=None, max_length=20, null=True)),
                ('width', models.IntegerField(default=None, null=True)),
                ('height', models.IntegerField(default=None, null=True)),
                ('qty', models.IntegerField(default=None, null=True)),
                ('rate', models.IntegerField(default=None, null=True)),
                ('payType', models.CharField(choices=[('PAID', 'paid'), ('FOC', 'foc')], default=None, max_length=20, null=True)),
                ('img', models.ImageField(upload_to='blockImg/Img/')),
            ],
        ),
    ]

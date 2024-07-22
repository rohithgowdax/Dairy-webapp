from django.db import models
from django.contrib.auth.models import User



CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'MilkShake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheez'),
    ('IC', 'Ice-Creams')
)
# Create your models here.
class Product(models.Model):
    title = models.CharField( max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField()
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product',null=True)

    def __str__(self) -> str:
        return self.title
    
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    locality = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    mobile =models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self) -> str:
        return self.name
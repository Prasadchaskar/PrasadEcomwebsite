from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    discrt = models.CharField(max_length=500)
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="Clothing")
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=30, default="")
    query = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

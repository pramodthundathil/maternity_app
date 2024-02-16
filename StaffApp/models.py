from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bills(models.Model):
    Billamount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.BooleanField(default=True)


from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    options = (
        ("1-4 weeks","1-4 weeks"),
        ("5-8 weeks","5-8 weeks"),
        ("9-13 weeks","9-13 weeks"),
        ("14-17 weeks","14-17 weeks"),
        ("18-22 weeks","18-22 weeks"),
        ("23-27 weeks","23-27 weeks"),
        ("28-31 weeks","28-31 weeks"),
        ("32-35 weeks","32-35 weeks"),
        ("36-40 weeks","36-40 weeks"),
 
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    MRP = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.FileField(upload_to='medicine_image')
    timester = models.CharField(max_length = 255, choices = options)
    
    
    def __str__(self):
        return str(self.name)
    


class CartItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stock = models.IntegerField()
    price = models.FloatField()
    
class CheckoutItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stock = models.IntegerField()
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)
    payment_status = models.BooleanField(default=False)
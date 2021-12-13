from django.db import models

# Create your models here.

class Details:
    id: int
    name: str
    img: str
    desc: str
    price: int

class Details(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics', default='rec1.jpg')
    desc = models.TextField(default='Hey! write here your branch.')
    year= models.IntegerField(default=2021)
    linkedin = models.CharField(max_length=200, default='www.linkedin.com')  
    facebook = models.CharField(max_length=200, default='www.facebook.com')    

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class ContactDetail(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Services(models.Model):
    service_title = models.CharField(max_length=500, default='')
    
    def __str__(self) -> str:
        return self.service_title
    
class Plan(models.Model):
    name = models.CharField(max_length=50)
    maxprice = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class PlanDetail(models.Model):
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
    detail = models.CharField(max_length=300)

    def __str__(self):
        return self.detail
    
class Review(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    plan = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    desc = models.TextField()
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    message = models.TextField()


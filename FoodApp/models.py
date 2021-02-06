from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


RATE_CHOICES = [
    ('Poor','Poor'),
    ('Average','Average'),
    ('Good','Good'),
    ('Excellent','Excellent')
]



DIET_CHOICES = [
    (1,'BreakFast'),
    (2,'Lunch'),
    (3,'Snacks'),
    (4,'Dinner')
]

class FoodModel(models.Model):
    item_name =  models.CharField(max_length=200,null=False,blank=False)
    item_image = models.ImageField(null=False,blank=True,upload_to='static/images/')
    item_desc = models.CharField(max_length = 200,null=False,blank = False)
    createdon = models.DateTimeField(default=now, editable=True)
    diet = models.SmallIntegerField(choices =DIET_CHOICES,null=False,blank=False)

    def __str__(self):
        return self.item_name   
    
    class Meta:
        ordering  = ('-createdon',)


class ReviewModel(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    foodmodel = models.ForeignKey(FoodModel,on_delete=models.CASCADE)
    createdon  = models.DateTimeField(default=now, editable=True)
    text = models.CharField(max_length = 600 , null=False,blank=True)
    rate = models.CharField(max_length=100,choices=RATE_CHOICES,default="Excellent")

    def __str__(self):
        return self.student.username


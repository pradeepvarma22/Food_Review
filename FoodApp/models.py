from django.db import models
from django.utils.timezone import now



RATE_CHOICES = [
    (1,'Poor'),
    (2,'Average'),
    (3,'Good'),
    (4,'Excellent')
]


DIET_CHOICES = [
    (1,'BreakFast'),
    (2,'Lunch'),
    (3,'Snacks'),
    (4,'Dinner')
]
        

#This Stores Food Items
class FoodModel(models.Model):
    #user = 
    item_name =  models.CharField(max_length=200,null=False,blank=False)
    item_image = models.ImageField(null=False,blank=True,upload_to='static/images/')
    item_desc = models.CharField(max_length = 200,null=False,blank = False)
    created_date = models.DateTimeField(default=now, editable=True)
    diet = models.SmallIntegerField(choices =DIET_CHOICES,null=False,blank=False)

    def __str__(self):
        return self.item_name
    
    class Meta:
        ordering  = ('-created_date',)


#This Stores Review For The items
class ReviewModel(models.Model):
    #user = 
    foodmodel = models.OneToOneField(FoodModel,on_delete=models.CASCADE,primary_key = True)
    created_date  = models.DateTimeField(default=now, editable=True)
    text = models.CharField(max_length = 600 , null=False,blank=False)
    rate = models.SmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return self.text


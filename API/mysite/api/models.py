from django.db import models

# Create your models here.
class Soulsborne(models.Model):
    # title = models.CharField(max_length=100)
    # published_content = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)
    # item_name = models.BooleanField(default=True)
    item_icon = models.CharField(max_length=100)
    item_name = models.CharField(max_length=50)
    # item_use = models.BooleanField(default=True)
    item_use = models.CharField(max_length=150)
    # item_availability = models.BooleanField(default=True)
    item_availability = models.CharField(max_length=250)
    item_description = models.TextField()
    category_type = models.CharField(max_length=50, null=True)
    # comments = models.TextField()
    # tags = models.CharField(max_length=25, null=True)
    
    def __str__(self):
        return self.title
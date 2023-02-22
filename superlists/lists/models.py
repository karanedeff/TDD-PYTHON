from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.TextField(default="")
    # TODO:
    #   adjust model so that items are associated with different lists

from django.db import models

# Create your models here.

class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
    # TODO:
    #   adjust model so that items are associated with different lists



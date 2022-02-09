from django.db import models
from django.urls import reverse

class Item(models.Model):
    text = models.TextField(default='')



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})

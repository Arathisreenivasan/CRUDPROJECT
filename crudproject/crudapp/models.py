from django.db import models

# Create your models here.
# class Item(models.Model):
#     slno = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     desc = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name

class Form(models.Model):
        slno = models.CharField(max_length=200)
        name = models.CharField(max_length=200)
        desc = models.CharField(max_length=200)

        def __str__(self):
            return self.name
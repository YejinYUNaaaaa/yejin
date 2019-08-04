from django.db import models

class Blood(models.Model):
    barcode_data = models.IntegerField()
    barcode_type = models.CharField()

from django.db import models

class TestModel(models.Model):
    category = models.CharField(max_length=255, default=True)
    subcatgeory = models.CharField(max_length=255, default=True)
    name = models.CharField(max_length=255, default=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

# {"category": "models","subcatgeory": "CharField","name": "models.CharField","amount": "500"}
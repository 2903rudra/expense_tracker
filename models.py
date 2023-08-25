from django.db import models

# Create your models here.

class Expense(models.Model):
    name = models.CharField(max_length=100 ,default='rudra')
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.amount} - {self.date}"
    

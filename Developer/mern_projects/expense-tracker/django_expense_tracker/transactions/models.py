# transactions/models.py

from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('earning', 'Earning'),
        ('expense', 'Expense'),
    ]

    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.type} - {self.title}"

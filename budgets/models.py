from django.db import models
from itineraries.models import Itinerary

class Budget(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.itinerary.title} - {self.amount}"

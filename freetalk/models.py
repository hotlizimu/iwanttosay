from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Rooms(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999999)])

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"{self.number}"


class Messages(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"{self.message}"

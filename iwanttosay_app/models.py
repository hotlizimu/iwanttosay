from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Texts(models.Model):
    password = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999999)])
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Texts'

    def __str__(self):
        return f"{self.password}:{self.text}"

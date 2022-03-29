from django.contrib.auth.models import User
from django.db import models


class Good(models.Model):
    name_good = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField(default=100)
    color = models.IntegerField(default=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.good}, {self.user}'
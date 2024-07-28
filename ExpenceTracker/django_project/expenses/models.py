# Django files
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User



class Income(models.Model):
    typeof = models.CharField(
        max_length = 6,
        choices = {
            'salary': "Salary",
            'wage': "Wage",
            'other': "Other"
        },
        default = 'salary'
    )
    date = models.DateTimeField(default = timezone.now)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(
        max_length = 50,
        blank=True, 
        null=True
    )
    owner = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self) -> str:
        return f"Owner: {self.owner}\nType: {self.typeof}\nAmount: {self.amount}\nTime: {self.date}\nDescription: {self.description}"

    def get_absolute_url(self) -> str:
        return reverse('income', args=[str(self.owner.username)])


class Outcome(models.Model):
    typeof = models.CharField(
        max_length = 21,
        choices = {
            'food': "Food",
            'transportation': "Transportation",
            'savings': "Savings",
            'housing_and_utilities': "Housing and utilities",
            'clothing': "Clothing",
            'other': "Others"
        },
        default = 'food'
    )
    date = models.DateTimeField(default = timezone.now)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(
        max_length = 50,
        blank=True, 
        null=True
    )
    owner = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self) -> str:
        return f"Owner: {self.owner}\nType: {self.typeof}\nAmount: {self.amount}\nTime: {self.date}\nDescription: {self.description}"

    def get_absolute_url(self):
        return reverse('outcome', args=[str(self.owner.username)])

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import calendar
from django.contrib.auth.models import User


class Week(models.Model):
    week = models.IntegerField(validators=[MaxValueValidator(52), MinValueValidator(1)])
    year = models.IntegerField(default=2021, validators=[MinValueValidator(2020)])

    def __str__(self):
        return "Week {} of {}".format(self.week, self.year)

    class Meta:
      unique_together = ('week', 'year',)

    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super(Week, self).save(*args, **kwargs)
        if is_new:
          for i in range(0, 5):
            day = Day(week=self, day=i)
            day.save()


class Day(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.IntegerField()

    def __str__(self):
        return "{} of week {} of {}".format(calendar.day_name[self.day], self.week.week, self.week.year)

    class Meta:
      unique_together = ('week', 'day',)


class Expense(models.Model):
    week = models.ForeignKey(Week, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(0)])
    comments = models.TextField(default="")

    def __str__(self):
        return "{}€ paid by {} in week {} of {}".format(self.amount, self.user, self.week.week, self.week.year)

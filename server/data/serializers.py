from .models import Week, Day, Expense
from rest_framework import serializers
import calendar


class WeekSerializer(serializers.HyperlinkedModelSerializer):
    days = serializers.SerializerMethodField()
    expenses = serializers.SerializerMethodField()

    class Meta:
        model = Week
        fields = "__all__"

    def get_days(self, obj):
        days = Day.objects.filter(week=obj)
        return DayOfWeekSerializer(days, many=True, context=self.context).data

    def get_expenses(self, obj):
        expenses = Expense.objects.filter(week=obj)
        return ExpenseSerializer(expenses, many=True, context=self.context).data


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = "__all__"


class DayOfWeekSerializer(serializers.HyperlinkedModelSerializer):
    day_name = serializers.SerializerMethodField()

    class Meta:
        model = Day
        fields = ["url", "day_name"]

    def get_day_name(self, obj):
        return calendar.day_name[obj.day]


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.SerializerMethodField()
    amount_euro = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields = ["url", "username", "amount_euro", "week", "user", "id", "comments"]

    def get_username(self, obj):
        return obj.user.username

    def get_amount_euro(self, obj):
        return "{}€".format(obj.amount)

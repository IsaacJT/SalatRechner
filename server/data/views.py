from rest_framework import viewsets
from rest_framework import permissions
from .models import Week, Day, Expense
from .serializers import WeekSerializer, DaySerializer, ExpenseSerializer


class WeekViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Week.objects.all().order_by("-year", "-week")
    serializer_class = WeekSerializer
    permission_classes = [permissions.IsAuthenticated]


class DayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Day.objects.all().order_by("-week", "day")
    serializer_class = DaySerializer
    permission_classes = [permissions.IsAuthenticated]


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

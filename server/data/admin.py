from django.contrib import admin
from data.models import Week, Day

# Register your models here.

class WeekAdmin(admin.ModelAdmin):
    pass

admin.site.register(Week, WeekAdmin)

class DayAdmin(admin.ModelAdmin):
    pass

admin.site.register(Day, DayAdmin)
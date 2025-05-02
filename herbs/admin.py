from django.contrib import admin
from .models import Herb, Category, HealthTracker
# Register your models here.
admin.site.register(Herb)
admin.site.register(Category)
admin.site.register(HealthTracker)
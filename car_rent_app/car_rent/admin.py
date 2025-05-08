from django.contrib import admin
from .models import *

# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):

    readonly_fields = ('user',)

    list_display = ("name", "location")

    def get_queryset(self, request):
        return Manufacturer.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        return super().save_model(request, obj, form, change)


class CarAdmin(admin.ModelAdmin):
    list_display = ("car_model", "manufacturer")

    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
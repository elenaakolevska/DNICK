from django.contrib import admin

from car_app.models import ServicePlace, Manufacturer, Service, ServicePlaceManufacturer, Car


# Register your models here.

class ServicePlaceManufacturerInline(admin.TabularInline):
    model = ServicePlaceManufacturer
    extra = 0

class ServicePlaceAdmin(admin.ModelAdmin):
    inlines = [ServicePlaceManufacturerInline,]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def has_add_permission(self, request):
        return request.user.is_superuser


class ServiceAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ServiceAdmin, self).save_model(request, obj, form, change)

class CarAdmin(admin.ModelAdmin):

    list_display = ("type", "speed",)


admin.site.register(ServicePlace, ServicePlaceAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
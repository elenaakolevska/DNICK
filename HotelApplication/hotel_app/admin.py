from django.contrib import admin
from django.template.context_processors import request

from hotel_app.models import RoomEmployee, Employee, Room, Reservation


# Register your models here.

class RoomEmployeeInline(admin.TabularInline):
    model = RoomEmployee
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "is_cleaned")

    #- Уредување/промена на соба може да прави само хигиеничар, а додавање соба само
    #суперкорисник

    def has_change_permission(self, request, obj=None):
        return Employee.objects.filter(type="H", user=request.user).exists()


    def has_add_permission(self, request):
        return request.user.is_superuser


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ("user",)
    inlines = [RoomEmployeeInline,]

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        return super(EmployeeAdmin, self).save_model(request, obj, form, change)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ("code", "room")
    exclude = ("user",)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False

            # Уредување/промена на резервацијата може да направи лицето што резервира,
            # рецепционер или менаџер во хотелот
        return obj and obj.employee.type=="M" or obj.employee.type=="R"

    def save_model(self, request, obj, form, change):
        obj.user=request.user

        #При креирањето на резервацијата, корисникот се доделува автоматски според најавениот
# корисник во моментот на системот. Не треба да се дозволи резервирање на соба која не е
# исчистена.

        room = Room.objects.filter(is_cleaned=True, number=obj.room.number).exists()
        if room and not change:
            return super(ReservationAdmin, self).save_model(request, obj, form, change)
        return


admin.site.register(Room, RoomAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Reservation, ReservationAdmin)

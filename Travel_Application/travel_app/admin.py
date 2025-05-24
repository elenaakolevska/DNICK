from django.contrib import admin
from django.db.models import Count

from travel_app.models import Travel, Guide


class TravelAdmin(admin.ModelAdmin):

    exclude = ('guide',)

    def has_add_permission(self, request):
        return Guide.objects.filter(user=request.user).exists()

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False
        if obj.guide is None:
            return False
        return obj.guide.user == request.user

    def has_view_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        guide = Guide.objects.filter(user=request.user).first()

        if not guide:
            return

        obj.guide = guide

        guide_travel = Travel.objects.filter(guide=guide).all()

        if not change and guide_travel.count() == 5:
            return

        sum = 0
        for travel in guide_travel:
            sum += travel.price

        old_travel_obj = guide_travel.filter(id=obj.id).first()
        old_price = old_travel_obj.price if old_travel_obj else 0

        if not change and sum + obj.price - old_price > 50000:
            return

        if not change and Travel.objects.filter(place_name=obj.place_name).exists():
            return

        super(TravelAdmin, self).save_model(request, obj, form, change)


class GuideAdmin(admin.ModelAdmin):

    exclude = ('user',)
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(GuideAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(travel_count=Count('travel')).filter(travel_count__lt=3)
        return qs


admin.site.register(Travel, TravelAdmin)
admin.site.register(Guide, GuideAdmin)

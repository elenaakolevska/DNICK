from datetime import datetime
from xmlrpc.client import DateTime

from django.contrib import admin

from real_estate_app.models import CharacteristicsRealEstate, RealEstateAgent, Agent, RealEstate, Characteristics


# Register your models here.

class CharacteristicsRealEstateInline(admin.TabularInline):
    model = CharacteristicsRealEstate
    extra = 0

class RealEstateAgentInline(admin.TabularInline):
    model = RealEstateAgent
    extra = 0

class RealEstateAgentAdmin(admin.ModelAdmin):
    pass

class RealEstateAdmin(admin.ModelAdmin):
    list_display = ("name", "area", "location",)
    inlines = [CharacteristicsRealEstateInline, RealEstateAgentInline,]

    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            RealEstateAgent.objects.create(real_estate=obj, agent = Agent.objects.filter(user=request.user).first())

    def has_delete_permission(self, request, obj=None):
        return not CharacteristicsRealEstate.objects.filter(real_estate=obj).exists()

    def has_change_permission(self, request, obj=None):
        return obj and  RealEstateAgent.objects.filter(real_estate=obj, agent__user=request.user).exists()

    def has_view_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        qs = super(RealEstateAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs.filter(date=datetime.now().date())
        return qs

class AgentAdmin(admin.ModelAdmin):
    exclude = ("user",)
    list_display = ("name", "surname",)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)



class CharacteristicsAdmin(admin.ModelAdmin):

    list_display = ("name",)

    def has_add_permission(self, request):
        return request.user.is_superuser




admin.site.register(Agent, AgentAdmin)
admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Characteristics, CharacteristicsAdmin)

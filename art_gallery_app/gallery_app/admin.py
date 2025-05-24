from django.contrib import admin

from gallery_app.models import Artist, Artwork, Exhibition


# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ArtistAdmin, self).save_model(request, obj, form, change)

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("title", "description",)

    def has_add_permission(self, request):
        return True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ArtworkAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ExhibitionAdmin, self).save_model(request, obj, form, change)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)


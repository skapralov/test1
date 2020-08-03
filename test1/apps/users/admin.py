from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)

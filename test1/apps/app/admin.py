from django.contrib import admin

from .models import Request, Offer


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass

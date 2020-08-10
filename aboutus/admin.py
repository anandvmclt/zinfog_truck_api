from django.contrib import admin
from .models import AboutUs


# Register your models here.
class AboutusAdmin(admin.ModelAdmin):
    list_display = ['yourName', 'source', 'pickUpFrom', 'deliveryTo', 'emailId', 'phoneNo', 'truckType', 'ord_status']
    actions = ['reject_orders', 'confirm_orders']

    def reject_orders(self, request, queryset):
            queryset.update(ord_status=AboutUs.REJECTED)
    reject_orders.short_description = "Reject selected orders"

    def confirm_orders(self, request, queryset):
            queryset.update(ord_status=AboutUs.CONFIRMED)
    confirm_orders.short_description = "Confirm selected orders"


admin.site.register(AboutUs, AboutusAdmin)

from django.contrib import admin
from .models import AboutUs
from django.contrib import messages
from django.forms import Textarea
from django.db import models

# Updating the Administration Texts
admin.site.site_header = "Zinfog Admin"
admin.site.site_title = "Zinfog Admin Portal"
admin.site.index_url = "https://zinfog.com/"
admin.site.index_title = "Welcome to Zinfog Truck Hiring Portal"

# Register your models here.
class AboutusAdmin(admin.ModelAdmin):
    list_display = ['yourName', 'source', 'pickUpFrom', 'deliveryTo', 'emailId', 'phoneNo', 'truckType', 'ord_status']
    actions = ['reject_orders', 'confirm_orders']

    def reject_orders(self, request, queryset):
            count =  queryset.update(ord_status=AboutUs.REJECTED)
            messages.info(request, 'Your Order has been Rejected!')
            print("Order data:",  queryset)
    reject_orders.short_description = "Reject selected orders"

    def confirm_orders(self, request, queryset):
            queryset.update(ord_status=AboutUs.CONFIRMED)
            messages.info(request, 'Your Order has been Approved!')
    confirm_orders.short_description = "Confirm selected orders"

    # def has_add_permission(self, request):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     return False
    @classmethod
    def has_add_permission(cls, request):
        ''' remove add and save and add another button '''
        return False

    def change_view(self, request, object_id, extra_context=None):
        ''' customize add/edit form '''
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = True
        return super(AboutusAdmin, self).change_view(request, object_id, extra_context=extra_context)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 36})},
    }


admin.site.register(AboutUs, AboutusAdmin)

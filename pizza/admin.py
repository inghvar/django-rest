from django.contrib import admin
from .models import Pizza, Order


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('pizza_size', )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_address' )


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order, OrderAdmin)

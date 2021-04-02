from django.contrib import admin

from .models import Customer, Product, Order, OrderItem, ShippingAddress

admin.site.register(Customer)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


# class ProductInline(admin.StackedInline):
#     model = Product
#     extra = 5


admin.site.register(Product)
# admin.site.register(ProductInline)

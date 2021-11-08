from django.db import models
from django.conf import settings
from products.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PAID = 'PD'
    PROCEEDED = 'PRD'
    READY = 'RDY'
    CANCELLED = 'CNC'

    ORDER_CHOICES = (
        (FORMING, 'in process'),
        (SEND_TO_PROCEED, 'sent to proceed'),
        (PAID, 'paid'),
        (PROCEEDED, 'proceeded'),
        (READY, 'ready to delivery'),
        (CANCELLED, 'cancelled')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated', auto_now_add=True)
    status = models.CharField(verbose_name='status', max_length=3, default=FORMING, choices=ORDER_CHOICES)
    is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return f'current order is {self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.get_product_cost(), items)))

    def delete(self, using=None, keep_parents=False):
        for item in self.orderitems.select_related():
            item.products.quantity += item.quantity
            item.products.save()
        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)

    def get_product_cost(self):
        return self.products.price * self.quantity

    def __str__(self):
        return f'current order is {self.pk}'

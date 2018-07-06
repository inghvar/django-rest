from django.db import models

class Pizza(models.Model):
    pizza_size = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Pizza'
        verbose_name = 'Pizzas'

    def __str__(self):
        return str(self.pizza_size)


class Order(models.Model):
    pizza = models.ManyToManyField(Pizza)
    customer_name = models.CharField(max_length=80)
    customer_address = models.TextField()

    class Meta:
        verbose_name_plural = 'Order'
        verbose_name = 'Orders'

    def __str__(self):
        return self.customer_name



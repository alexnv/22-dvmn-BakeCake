from django.db import models


class Layer(models.Model):
    num_layers = models.IntegerField(
        'Количество слоев',
    )
    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.num_layers}"

    class Meta:
        verbose_name = 'Опция количества слоев'
        verbose_name_plural = 'Опции количества слоев'


class Shape(models.Model):
    name = models.CharField(
        'Описание формы',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция формы'
        verbose_name_plural = 'Опции формы'


class Topping(models.Model):
    name = models.CharField(
        'Описание топпинга',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция топпинга'
        verbose_name_plural = 'Опции топпинга'


class Berries(models.Model):
    name = models.CharField(
        'Описание ягод',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция ягод'
        verbose_name_plural = 'Опции ягод'


class Decor(models.Model):
    name = models.CharField(
        'Описание украшения',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0,
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция украшения'
        verbose_name_plural = 'Опции украшения'

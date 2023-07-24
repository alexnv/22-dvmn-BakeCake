from django.contrib.auth.models import User
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


class Customers(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Имя заказчика',
        on_delete=models.CASCADE,
        related_name='customer'
    )
    phone = models.TextField('Номер телефона')
    address = models.TextField('Адрес заказчика')

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'


class Orders(models.Model):
    PAYMENT = 'Payment'
    PREPARING = 'Preparing'
    IN_DELIVERY = 'In delivery'
    COMPLETED = 'Completed'

    STATUSES = [
        (PAYMENT, 'Ожидает оплаты'),
        (PREPARING, 'Готовится'),
        (IN_DELIVERY, 'Доставляется'),
        (COMPLETED, 'Завершен'),
    ]

    layer = models.ForeignKey(
        Layer,
        verbose_name='Уровень',
        on_delete=models.CASCADE
    )
    shape = models.ForeignKey(
        Shape,
        verbose_name='Форма',
        on_delete=models.CASCADE
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name='топпинг',
        on_delete=models.CASCADE
    )
    berry = models.ForeignKey(
        Berries,
        verbose_name='Ягоды',
        on_delete=models.CASCADE,
        blank=True
    )
    decor = models.ForeignKey(
        Decor,
        verbose_name='Декор',
        on_delete=models.CASCADE,
        blank=True
    )

    price = models.DecimalField(
        'Цена',
        default=0,
        max_digits=10,
        decimal_places=2
    )

    word = models.TextField(verbose_name='Надпись на торте')
    comment = models.TextField('Комментарий к заказу', blank=True)
    customer = models.ForeignKey(
        Customers,
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        related_name='orders',
        default=None
    )
    date_delivery = models.DateField('Дата доставки')
    time_delivery = models.TimeField('Время доставки')

    status = models.CharField(
        'Статус заказа',
        max_length=20,
        choices=STATUSES,
        default=PAYMENT,
    )

    def __str__(self) -> str:
        return f"{self._check_id_field()}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class UtmCheckin(models.Model):
    check_in_date = models.DateTimeField('Время захода', auto_now=True)
    utm_source = models.CharField('Источник UTM', max_length=100)
    utm_medium = models.CharField('Тип траффика', max_length=10)
    utm_campaign = models.CharField('Название компании', max_length=100)
    utm_content = models.CharField('Идентификатор объявления', max_length=250)
    utm_term = models.CharField('Ключевое слово', max_length=100)

    class Meta:
        verbose_name = 'UTM метка'
        verbose_name_plural = 'UTM метки'

    def str(self):
        return self.utm_source

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Status(models.Model):
    """
    Модель для хранения статуса обработка заказа.
    --------
    Атрибуты
    --------
    status: CharField
        статус
    note: TextFieldss
        текст, описывающий устройство
    """

    status = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Статус'
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание(Пимечание)'
    )

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ('status',)

    def __str__(self):
        return f'{self.status}'

class Location(models.Model):
    """
    Модель для хранения населенных пунктов.
    --------
    Атрибуты
    --------
    location: CharField
        название НП
    note: TextFieldss
        текст, описывающий НП
    """

    title = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Населенный пункт'
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание(Пимечание)'
    )

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
        ordering = ('title',)

    def __str__(self):
        return f'{self.title}'

class Unit(models.Model):
    """
    Модель для хранения подразделениий.
    --------
    Атрибуты
    --------
    title: CharField
        название подразделения
    location: ForeignKey
        НП, где находится подразделение
    street: TextFieldss
        улица
    num: TextFieldss
        номер дома
    """

    title = models.CharField(
        max_length=50,
        verbose_name='Подразделение'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='units',
        verbose_name='Населеный пункт'
    )
    street = models.CharField(
        max_length=50,
        verbose_name='Улица'
    )
    num = models.CharField(
        max_length=5,
        verbose_name='Номер дома'
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ('title', 'location',)
    
    def __str__(self):
        return f'{self.title}'    


class Device(models.Model):
    """
    Модель для хранения устройств.
    --------
    Атрибуты
    --------
    device: CharField
        утсройство
    note: TextFieldss
        текст, описывающий устройство
    """

    title = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Устройство'
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание(Пимечание)'
    )

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'
        ordering = ('title',)

    def __str__(self):
        return f'{self.title}'


class Bid(models.Model):
    """
    Модель для хранения заявок.
    --------
    Атрибуты
    --------
    text: TextField
        текст заявки
    pub_date: DateTimeField
        дата публикации заявки
    user: ForeignKey
        автор заявки(подразделение+кабинет)
    device: ForeignKey
        что сломалось
    """

    text = models.TextField(
        verbose_name='Заявка',
        help_text='Опишите проблему'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bids',
        verbose_name='Пользователь'
    )
    device = models.ForeignKey(
        Device,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='bids',
        verbose_name='Устройство',
        help_text='Укажите устройство'
    )
    status = models.ForeignKey(
        Status,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='bids',
        verbose_name='Статус',
        help_text='ПОСЛЕ ОБРАБОТКИ ЗАПРОСА ПОМЕНЙТЕ СТАТУС!!!'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='bid/',
        blank=True,
        help_text='Вы можете загрузить изображение'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-pub_date',)

    def __str__(self):
        return f'{self.status, self.user, self.text[:15]}'

class Worker(models.Model):
    """
    Модель для хранения информации о сотрудниках отдела КО.
    --------
    Атрибуты
    --------
    last_name: CharField
        Фамилия
    name: CharField
        Имя
    fathers_name: CharField
        Отчество
    dob: DateTimeField
        Дата рождениия
    """
    last_name = models.CharField(
        max_length=40,
        verbose_name='Фамилия'
    )
    name = models.CharField(
        max_length=40,
        verbose_name='Имя'
    )
    fathers_name = models.CharField(
        max_length=40,
        verbose_name='Отчество'
    )
    dob = models.DateField(
        verbose_name='Дата рождениия'
    )
    class Meta:
        verbose_name = 'Сотрудник отдела'
        verbose_name_plural = 'Сотрудники отдела'
        ordering = ('last_name','name',)

    def __str__(self):
        return f'{self.last_name}'


class Level(models.Model):
    """
    Модель для хранения уровней важности.
    --------
    Атрибуты
    --------
    level: CharField
        уровень важности
    note: TextFieldss
        текст, описывающий уровень
    """

    level = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Уровень важности',
        default='Штатный'
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание(Пимечание)'
    )

    class Meta:
        verbose_name = 'Уровень важности'
        verbose_name_plural = 'Уровни важности'
        ordering = ('level',)

    def __str__(self):
        return f'{self.level}'


class Control(models.Model):
    """
    Модель для обработки заявок.
    --------
    Атрибуты
    --------
    bid: ForeignKey
        заявка
    worker: ForeignKey
        сотрудник-ответсвенный
    level: ForeignKey
        уровень важности
    date: DateTimeField
        дата
    note: TextFieldss
        заметки(примечание)
    """

    bid = models.OneToOneField(
        Bid,
        on_delete=models.CASCADE,
        null = True,
        default = 'NULL',
        related_name='controls',
        verbose_name='Заявка',
        help_text='Укажите обрабатываемую заявку'
    )
    worker = models.ForeignKey(
        Worker,
        on_delete=models.SET_DEFAULT,
        null = True,
        default = 'NULL',
        related_name='controls',
        verbose_name='Ответсвенный сотрудник',
        help_text='Укажите ответсвенного сотрудника'
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.SET_DEFAULT,
        null = True,
        default = 'NULL',
        related_name='controls',
        verbose_name='Уровень важности'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание(Пимечание)'
    )

    class Meta:
        verbose_name = 'Обработка заявки'
        verbose_name_plural = 'Обработка заявок'
        ordering = ('bid',)

    def __str__(self):
        return f'{self.bid}'
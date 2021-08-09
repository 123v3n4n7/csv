from django.db import models


class CSVObject(models.Model):
    code = models.CharField(max_length=15, verbose_name='Код', blank=True)
    name = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    level_1 = models.CharField(max_length=50, verbose_name='Уровень 1', blank=True)
    level_2 = models.CharField(max_length=50, verbose_name='Уровень 2', blank=True)
    level_3 = models.CharField(max_length=50, verbose_name='Уровень 3', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=5, null=True, verbose_name='Цена')
    price_sp = models.DecimalField(max_digits=10, decimal_places=5, null=True, verbose_name='Цена СП')
    amount = models.IntegerField(null=True, verbose_name='Количество')
    fields_of_options = models.TextField(verbose_name='Поля свойств', blank=True)
    joint_purchases = models.IntegerField(null=True, verbose_name='Совместные покупки')
    unit = models.CharField(max_length=15, verbose_name='Единица измерения', blank=True)
    image = models.CharField(max_length=100, verbose_name='Картинка', blank=True)
    show_on_main_page = models.IntegerField(null=True, verbose_name='Выводить на главной', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.code}  {self.name}'

    class Meta:
        verbose_name = "CSVObject"
        verbose_name_plural = "CSVObjects"

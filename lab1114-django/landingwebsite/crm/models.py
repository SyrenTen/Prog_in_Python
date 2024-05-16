from django.db import models


class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Назва статусу')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статуси"


# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Ім'я")
    order_phone = models.CharField(max_length=200, verbose_name="Телефон")
    order_email = models.CharField(max_length=200, verbose_name="Email")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Cтатус")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Всі замовлення"


class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='Текст коментаря')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата створення')

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"




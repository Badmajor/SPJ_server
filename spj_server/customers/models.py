from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Country(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Requisites(models.Model):
    tin = models.CharField(max_length=20)
    title = models.CharField(max_length=256)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True
    )
    address = models.TextField()


class Customer(models.Model):
    name = models.CharField(max_length=256)
    requisites = models.OneToOneField(
        Requisites,
        null=False,
        blank=False,
        unique=True,
        on_delete=models.PROTECT
    )
    candidates = models.ManyToManyField(
        User,
        blank=True,
        through='CustomerUser',
        related_name='respond'
    )
    is_published = models.BooleanField(
        default=True
    )
    responsible = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    @property
    def success(self):
        return CustomerUser.objects.filter(
            customer=self,
            success=True,
        ).count()

    @property
    def request_count(self):
        return CustomerUser.objects.filter(
            customer=self
        ).count()

    registration_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        default_related_name = 'customer'

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    url_repository = models.URLField()
    users = models.ManyToManyField(
        User,
        blank=True,
        through='UserTask',
    )


class Vacancy(models.Model):
    title = models.CharField(max_length=256)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING
    ) # при удалении ничего не делаем, по количеству вакансий ведем статистику
    candidates = models.ManyToManyField(
        User,
        blank=True,
        through='CustomerUser',
    )
    is_published = models.BooleanField(
        default=True
    )
    registration_date = models.DateTimeField(
        auto_now_add=True
    )
    task = models.OneToOneField(
        Task,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posted_vacancy'
    )
    # добавить поле с форматом работы (удаленка и пр.)
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        default_related_name = 'vacancy'

    def __str__(self):
        return self.title


class CustomerUser(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    success = models.BooleanField(default=False)
    date = models.DateTimeField(
        auto_now_add=True
    )
    vacancies = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE
    )
    class Meta:
        unique_together = ('customer', 'user', 'vacancies')


class UserTask(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    success = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'task')


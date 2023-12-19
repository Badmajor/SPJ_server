from django.contrib.auth.models import AbstractUser
from django.db import models

class ProgrammingLanguage(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

# добавить ЯП, стек фреймворков, опыт, грейд(user выставляет сам)

class CustomUser(AbstractUser):
    company = models.ForeignKey(
        'customers.Customer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    pr_language = models.ForeignKey(
        ProgrammingLanguage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    def __str__(self):
        return self.username
from django.db import models


class Teammate(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    key = models.ForeignKey('Team', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name = 'Состав команды'
        verbose_name_plural = 'Состав команды'


class Team(models.Model):
    team_name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = 'Команды'
        verbose_name_plural = 'Команды'


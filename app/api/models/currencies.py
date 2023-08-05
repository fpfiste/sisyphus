from django.db import models


class Currencies(models.Model):
    id_currency = models.AutoField(primary_key=True)
    currency = models.CharField()
    currency_abbreviation = models.CharField()
    currency_account_nr = models.CharField()

    class Meta:
        managed = False
        db_table = 'currencies'
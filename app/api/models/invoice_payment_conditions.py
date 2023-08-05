from django.db import models




class PaymentConditions(models.Model):
    id_payment_condition = models.AutoField(primary_key=True)
    vat = models.DecimalField(max_digits=65535, decimal_places=65535)
    fk_currency = models.ForeignKey('Currencies', models.DO_NOTHING, db_column='fk_currency')
    due_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_conditions'
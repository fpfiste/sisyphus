from django.db import models



class InvoiceStates(models.Model):
    id_invoice_state = models.AutoField(primary_key=True)
    invoice_state = models.CharField()
    invoice_state_abbreviation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_states'
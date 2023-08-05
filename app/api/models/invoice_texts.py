from django.db import models


class InvoiceTexts(models.Model):
    id_invoice_text = models.AutoField(primary_key=True)
    invoice_text = models.CharField()
    fk_customer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_texts'

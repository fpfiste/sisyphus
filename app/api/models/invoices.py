from django.db import models



class Invoices(models.Model):
    id_invoice = models.AutoField(primary_key=True)
    invoice_date = models.DateField(blank=True, null=True)
    fk_invoice_text = models.ForeignKey('InvoiceTexts', models.DO_NOTHING, db_column='fk_invoice_text', blank=True, null=True)
    fk_invoice_state = models.ForeignKey('InvoiceStates', models.DO_NOTHING, db_column='fk_invoice_state')
    fk_payment_conditions = models.ForeignKey('PaymentConditions', models.DO_NOTHING, db_column='fk_payment_conditions')

    class Meta:
        managed = False
        db_table = 'invoices'
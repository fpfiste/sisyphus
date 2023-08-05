from django.db import models






class Sales(models.Model):
    id_sale = models.AutoField(primary_key=True)
    sale_timestamp = models.DateTimeField()
    fk_project = models.ForeignKey('Projects', models.DO_NOTHING, db_column='fk_project')
    sale_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    sale_unit_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    sales_reference = models.CharField()
    fk_unit = models.IntegerField()
    fk_product = models.IntegerField()
    fk_invoice = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales'

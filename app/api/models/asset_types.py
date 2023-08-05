from django.db import models






class AssetTypes(models.Model):
    id_asset_type = models.AutoField(primary_key=True)
    asset_type = models.CharField()
    max_capacity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_types'
